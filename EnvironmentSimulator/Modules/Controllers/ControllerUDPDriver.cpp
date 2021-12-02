/*
 * esmini - Environment Simulator Minimalistic
 * https://github.com/esmini/esmini
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 *
 * Copyright (c) partners of Simulation Scenarios
 * https://sites.google.com/view/simulationscenarios
 */

/*
 * This controller simulates a bad or dizzy driver by manipulating
 * the speed and lateral offset in a random way.
 * The purpose is purely to demonstrate how to implement a controller.
 */

#include "ControllerUDPDriver.hpp"
#include "CommonMini.hpp"
#include "Entities.hpp"
#include "ScenarioGateway.hpp"

#include <random>

using namespace scenarioengine;

int ControllerUDPDriver::basePort_ = DEFAULT_UDP_DRIVER_PORT;

Controller* scenarioengine::InstantiateControllerUDPDriver(void* args)
{
	Controller::InitArgs* initArgs = (Controller::InitArgs*)args;

	return new ControllerUDPDriver(initArgs);
}

ControllerUDPDriver::ControllerUDPDriver(InitArgs* args) :
	inputMode_(InputMode::DRIVER_INPUT), udpServer_(nullptr), port_(0), execMode_(ExecMode::EXEC_MODE_ASYNCHRONOUS), Controller(args)
{
	if (args && args->properties && args->properties->ValueExists("inputMode"))
	{
		if (args->properties->GetValueStr("inputMode") == "vehicleStateXYH")
		{
			inputMode_ = InputMode::VEHICLE_STATE_XYH;
		}
		else if (args->properties->GetValueStr("inputMode") == "vehicleStateXYZHPR")
		{
			inputMode_ = InputMode::VEHICLE_STATE_XYZHPR;
		}
		else if (args->properties->GetValueStr("inputMode") == "driverInput")
		{
			inputMode_ = InputMode::DRIVER_INPUT;
		}
		else
		{
			LOG_AND_QUIT("ControllerExternalDriverModel unexpected arg inputMode %s",
				args->properties->GetValueStr("inputMode").c_str());
		}
	}

	if (args && args->properties && args->properties->ValueExists("port"))
	{
		int portTmp = strtoi(args->properties->GetValueStr("port"));
		if (portTmp < 0 || portTmp > 65535)
		{
			LOG_AND_QUIT("Invlaid driver model port: %d (valid range is [0, 65535]", portTmp);
		}
		else
		{
			port_ = (unsigned short)portTmp;
		}
	}

	if (args && args->properties && args->properties->ValueExists("basePort"))
	{
		int basePortTmp = strtoi(args->properties->GetValueStr("basePort"));
		if (basePortTmp < 0 || basePortTmp > 65535)
		{
			LOG_AND_QUIT("Invlaid driver model basePort: %d (valid range is [0, 65535]", basePortTmp);
		}
		else if (basePortTmp != basePort_)
		{
			LOG("Changing base port to %d (from %d)", basePortTmp, basePort_);
			basePort_ = basePortTmp;
		}
	}

	if (args && args->properties && args->properties->ValueExists("execMode"))
	{
		if (args->properties->GetValueStr("execMode") == "asynchronous")
		{
			execMode_ = ExecMode::EXEC_MODE_ASYNCHRONOUS;
		}
		else if (args->properties->GetValueStr("execMode") == "synchronous")
		{
			execMode_ = ExecMode::EXEC_MODE_SYNCHRONOUS;
		}
		else
		{
			LOG_AND_QUIT("ControllerExternalDriverModel unexpected arg execMode %s",
				args->properties->GetValueStr("execMode").c_str());
		}
	}

	// currently only supporting override mode
	if (args && args->properties && args->properties->ValueExists("mode"))
	{
		if (args->properties->GetValueStr("intputMode") == "additive")
		{
			LOG("ExternalDriverModelController only support override mode, ignoring requested additive mode");
		}
	}
	mode_ = Mode::MODE_OVERRIDE;

	memset((void*)&msg, 0, sizeof(msg));
	memset((void*)&lastMsg, 0, sizeof(lastMsg));
}

ControllerUDPDriver::~ControllerUDPDriver()
{
	if (udpServer_ != nullptr)
	{
		delete udpServer_;
	}
}

std::string ControllerUDPDriver::InputMode2Str(InputMode inputMode)
{
	if (inputMode == InputMode::DRIVER_INPUT)
	{
		return "driverInput";
	}
	else if (inputMode == InputMode::VEHICLE_STATE_XYH)
	{
		return "vehicleStateXYH";
	}
	else if (inputMode == InputMode::VEHICLE_STATE_XYZHPR)
	{
		return "vehicleStateXYZHPR";
	}
	else
	{
		return "Unknown";
	}
}

std::string ControllerUDPDriver::ExecMode2Str(ExecMode execMode)
{
	if (execMode == ExecMode::EXEC_MODE_ASYNCHRONOUS)
	{
		return "Asynchronous";
	}
	else if (execMode == ExecMode::EXEC_MODE_SYNCHRONOUS)
	{
		return "Synchronous";
	}
	else
	{
		return "Unknown";
	}
}

void ControllerUDPDriver::Init()
{
	if (basePort_ == -1)
	{
		basePort_ = DEFAULT_UDP_DRIVER_PORT;
		LOG("ControllerUDPDriver: using default baseport %d", basePort_);
	}
	Controller::Init();
}

void ControllerUDPDriver::Step(double timeStep)
{
	int retval = 0;
	int receivedNrOfBytes = 0;

	if (execMode_ == ExecMode::EXEC_MODE_ASYNCHRONOUS)
	{
		// Pick all queued messages - store only the last/latest
		while (retval >= 0)
		{
			retval = udpServer_->Receive((char*)&msg, sizeof(msg));
			if (retval > 0)
			{
				receivedNrOfBytes = retval;
			}
		}
	}
	else
	{
		retval = udpServer_->Receive((char*)&msg, sizeof(msg));
		if (retval >= 0)
		{
			receivedNrOfBytes = retval;
		}
	}

	if (receivedNrOfBytes > 0)
	{
		lastMsg = msg;

		//printf("version %d objectId %d framenr %d inputMode %d/%s \n",
		//	msg.header.version,
		//	msg.header.objectId,
		//	msg.header.frameNumber,
		//	msg.header.inputMode,
		//	InputMode2Str(static_cast<InputMode>(msg.header.inputMode)).c_str());

		if (msg.header.version != UDP_DRIVER_MESSAGE_VERSION)
		{
			LOG_ONCE("ControllerUDPDriver: Got unsupported msg version %d (only accepting version %d)",
				msg.header.version, UDP_DRIVER_MESSAGE_VERSION);
		}

		if (msg.header.inputMode == static_cast<int>(InputMode::VEHICLE_STATE_XYZHPR))
		{
			roadmanager::Position* pos = &gateway_->getObjectStatePtrById(msg.header.objectId)->state_.pos;
			pos->SetAlignModeZ(roadmanager::Position::ALIGN_MODE::ALIGN_NONE);
			pos->SetAlignModeP(roadmanager::Position::ALIGN_MODE::ALIGN_NONE);

			// Update object state via gateway
			gateway_->updateObjectWorldPos(object_->id_, 0.0, msg.message.stateXYZHPR.x, msg.message.stateXYZHPR.y, msg.message.stateXYZHPR.z,
				msg.message.stateXYZHPR.h, msg.message.stateXYZHPR.p, msg.message.stateXYZHPR.r);
			gateway_->updateObjectSpeed(object_->id_, 0.0, msg.message.stateXYZHPR.speed);
			gateway_->updateObjectWheelAngle(object_->id_, 0.0, msg.message.stateXYZHPR.wheelAngle);

			// Also update the internal vehicle model, in case next message is driver input
			vehicle_.SetPos(msg.message.stateXYZHPR.x, msg.message.stateXYZHPR.y, msg.message.stateXYZHPR.z, msg.message.stateXYZHPR.h);
		}
		else if (msg.header.inputMode == static_cast<int>(InputMode::VEHICLE_STATE_XYH))
		{
			roadmanager::Position* pos = &gateway_->getObjectStatePtrById(msg.header.objectId)->state_.pos;
			pos->SetAlignModeZ(roadmanager::Position::ALIGN_MODE::ALIGN_HARD);
			pos->SetAlignModeP(roadmanager::Position::ALIGN_MODE::ALIGN_HARD);

			// Update object state via gateway
			gateway_->updateObjectWorldPosXYH(object_->id_, 0.0, msg.message.stateXYH.x, msg.message.stateXYH.y, msg.message.stateXYH.h);
			gateway_->updateObjectSpeed(object_->id_, 0.0, msg.message.stateXYH.speed);
			gateway_->updateObjectWheelAngle(object_->id_, 0.0, msg.message.stateXYH.wheelAngle);

			// Also update the internal vehicle model, in case next message is driver input
			vehicle_.SetPos(msg.message.stateXYH.x, msg.message.stateXYH.y, pos->GetZ(), msg.message.stateXYH.h);

			// Fetch Pitch from OpenDRIVE position
			vehicle_.SetPitch(pos->GetP());
		}
		else if (msg.header.inputMode == static_cast<int>(InputMode::DRIVER_INPUT))
		{
			roadmanager::Position* pos = &gateway_->getObjectStatePtrById(msg.header.objectId)->state_.pos;
			pos->SetAlignModeZ(roadmanager::Position::ALIGN_MODE::ALIGN_HARD);
			pos->SetAlignModeP(roadmanager::Position::ALIGN_MODE::ALIGN_HARD);
		}
		else
		{
			LOG("ControllerExternalDriverModel received %d bytes and unexpected input mode %d", retval, msg.header.inputMode);
		}
	}

	if (lastMsg.header.inputMode == static_cast<int>(InputMode::DRIVER_INPUT))
	{
		// In driver input mode the vehicle is updated continuously wrt latest input
		vehicle_.DrivingControlAnalog(timeStep, lastMsg.message.driverInput.throttle - lastMsg.message.driverInput.brake, lastMsg.message.driverInput.steeringAngle);

		// Register updated vehicle position
		gateway_->updateObjectWorldPosXYH(object_->id_, 0.0, vehicle_.posX_, vehicle_.posY_, vehicle_.heading_);
		gateway_->updateObjectSpeed(object_->id_, 0.0, vehicle_.speed_);
		gateway_->updateObjectWheelAngle(object_->id_, 0.0, msg.message.driverInput.steeringAngle);

		// Fetch Z and Pitch from OpenDRIVE position
		roadmanager::Position* pos = &gateway_->getObjectStatePtrById(msg.header.objectId)->state_.pos;
		vehicle_.SetZ(pos->GetZ());
		vehicle_.SetPitch(pos->GetP());
	}

	Controller::Step(timeStep);
}

void ControllerUDPDriver::Activate(ControlDomains domainMask)
{
	if (object_)
	{
		if (port_ == 0)   // port not specified, assign default
		{
			port_ = basePort_ + object_->GetId();
		}

		if (udpServer_ == nullptr ||  // not created yet
			(udpServer_ != nullptr && udpServer_->GetPort() != port_)) // port nr changed. Need to recreate the socket.
		{
			// Close socket in case the controller is assigned again with different port
			if (udpServer_ != nullptr)
			{
				delete udpServer_;
			}
			if (execMode_ == ExecMode::EXEC_MODE_ASYNCHRONOUS)
			{
				udpServer_ = new UDPServer((unsigned short)port_, 1);
			}
			else
			{
				udpServer_ = new UDPServer((unsigned short)port_, UDP_SYNCHRONOUS_MODE_TIMEOUT_MS);
			}
			LOG("ExternalDriverModel server listening on port %d execMode: %s", port_, ExecMode2Str(execMode_).c_str());
		}

		vehicle_.Reset();
		vehicle_.SetPos(object_->pos_.GetX(), object_->pos_.GetY(), object_->pos_.GetZ(), object_->pos_.GetH());
		vehicle_.SetLength(object_->boundingbox_.dimensions_.length_);
		vehicle_.speed_ = object_->GetSpeed();
		vehicle_.SetMaxAcc(20.0);
		vehicle_.SetMaxSpeed(30.0);
	}

	steer = vehicle::STEERING_NONE;
	accelerate = vehicle::THROTTLE_NONE;

	Controller::Activate(domainMask);
}

void ControllerUDPDriver::ReportKeyEvent(int key, bool down)
{
}
