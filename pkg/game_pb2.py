# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngame.proto\"&\n\x12SetUsernameRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"e\n\x13SetUsernameResponse\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.SetUsernameResponse.Status\"!\n\x06Status\x12\x06\n\x02Ok\x10\x00\x12\x0f\n\x0bNameIsTaken\x10\x01\"I\n\x13StartSessionRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x05\"\x8d\x01\n\x14StartSessionResponse\x12,\n\x06status\x18\x01 \x01(\x0e\x32\x1c.StartSessionResponse.Status\x12\x18\n\x04role\x18\x02 \x01(\x0e\x32\x05.RoleH\x00\x88\x01\x01\"$\n\x06Status\x12\x06\n\x02Ok\x10\x00\x12\x12\n\x0eWrongSessionID\x10\x01\x42\x07\n\x05_role\":\n\x12JoinSessionRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\"\x9e\x01\n\x13JoinSessionResponse\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.JoinSessionResponse.Status\x12\x18\n\x04role\x18\x02 \x01(\x0e\x32\x05.RoleH\x00\x88\x01\x01\"7\n\x06Status\x12\x06\n\x02Ok\x10\x00\x12\x12\n\x0eWrongSessionID\x10\x01\x12\x11\n\rSessionIsFull\x10\x02\x42\x07\n\x05_role\"$\n\x10MessengerRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"\xa6\x01\n\x11MessengerResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.MessengerResponse.Status\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x06victim\x18\x03 \x01(\tH\x00\x88\x01\x01\"5\n\x06Status\x12\x08\n\x04Join\x10\x00\x12\t\n\x05Start\x10\x01\x12\x08\n\x04Kill\x10\x02\x12\x0c\n\x08\x45nd_Game\x10\x03\x42\t\n\x07_victim\"d\n\x0f\x44\x61yNightRequest\x12#\n\x04time\x18\x01 \x01(\x0e\x32\x15.DayNightRequest.Time\x12\x10\n\x08username\x18\x02 \x01(\t\"\x1a\n\x04Time\x12\x07\n\x03\x44\x61y\x10\x00\x12\t\n\x05Night\x10\x01\"\xce\x01\n\x10\x44\x61yNightResponse\x12\x0e\n\x06victim\x18\x01 \x01(\t\x12\x1a\n\x0bvictim_role\x18\x02 \x01(\x0e\x32\x05.Role\x12\r\n\x05mafia\x18\x03 \x01(\t\x12*\n\x06is_end\x18\x04 \x01(\x0e\x32\x1a.DayNightResponse.GameOver\x12\x0e\n\x06\x61lives\x18\x05 \x03(\t\x12\x0e\n\x06ghosts\x18\x06 \x03(\t\"3\n\x08GameOver\x12\x0b\n\x07NotOver\x10\x00\x12\x0c\n\x08MafiaWin\x10\x01\x12\x0c\n\x08\x43ivilWin\x10\x02\">\n\x11KillPlayerRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x17\n\x0fvictim_username\x18\x02 \x01(\t\"\x14\n\x12KillPlayerResponse\"A\n\x14\x44\x65tectiveMoveRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x17\n\x0fvictim_username\x18\x02 \x01(\t\"3\n\x15\x44\x65tectiveMoveResponse\x12\x1a\n\x0bplayer_role\x18\x02 \x01(\x0e\x32\x05.Role\"5\n\x12PublishDataRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05mafia\x18\x02 \x01(\t\"\x15\n\x13PublishDataResponse\"\x1f\n\x0bInfoRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"-\n\x0cInfoResponse\x12\x0e\n\x06\x61lives\x18\x05 \x03(\t\x12\r\n\x05roles\x18\x06 \x03(\t*>\n\x04Role\x12\t\n\x05Mafia\x10\x00\x12\r\n\tDetective\x10\x01\x12\r\n\tCivillian\x10\x02\x12\r\n\tUndefined\x10\x03\x32\x8e\x04\n\x0cMafiaService\x12:\n\x0bSetUsername\x12\x13.SetUsernameRequest\x1a\x14.SetUsernameResponse\"\x00\x12=\n\x0cStartSession\x12\x14.StartSessionRequest\x1a\x15.StartSessionResponse\"\x00\x12:\n\x0bJoinSession\x12\x13.JoinSessionRequest\x1a\x14.JoinSessionResponse\"\x00\x12\x36\n\tMessenger\x12\x11.MessengerRequest\x1a\x12.MessengerResponse\"\x00\x30\x01\x12\x31\n\x08\x44\x61yNight\x12\x10.DayNightRequest\x1a\x11.DayNightResponse\"\x00\x12\x37\n\nKillPlayer\x12\x12.KillPlayerRequest\x1a\x13.KillPlayerResponse\"\x00\x12@\n\rDetectiveMove\x12\x15.DetectiveMoveRequest\x1a\x16.DetectiveMoveResponse\"\x00\x12:\n\x0bPublishData\x12\x13.PublishDataRequest\x1a\x14.PublishDataResponse\"\x00\x12%\n\x04Info\x12\x0c.InfoRequest\x1a\r.InfoResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROLE._serialized_start=1479
  _ROLE._serialized_end=1541
  _SETUSERNAMEREQUEST._serialized_start=14
  _SETUSERNAMEREQUEST._serialized_end=52
  _SETUSERNAMERESPONSE._serialized_start=54
  _SETUSERNAMERESPONSE._serialized_end=155
  _SETUSERNAMERESPONSE_STATUS._serialized_start=122
  _SETUSERNAMERESPONSE_STATUS._serialized_end=155
  _STARTSESSIONREQUEST._serialized_start=157
  _STARTSESSIONREQUEST._serialized_end=230
  _STARTSESSIONRESPONSE._serialized_start=233
  _STARTSESSIONRESPONSE._serialized_end=374
  _STARTSESSIONRESPONSE_STATUS._serialized_start=329
  _STARTSESSIONRESPONSE_STATUS._serialized_end=365
  _JOINSESSIONREQUEST._serialized_start=376
  _JOINSESSIONREQUEST._serialized_end=434
  _JOINSESSIONRESPONSE._serialized_start=437
  _JOINSESSIONRESPONSE._serialized_end=595
  _JOINSESSIONRESPONSE_STATUS._serialized_start=531
  _JOINSESSIONRESPONSE_STATUS._serialized_end=586
  _MESSENGERREQUEST._serialized_start=597
  _MESSENGERREQUEST._serialized_end=633
  _MESSENGERRESPONSE._serialized_start=636
  _MESSENGERRESPONSE._serialized_end=802
  _MESSENGERRESPONSE_STATUS._serialized_start=738
  _MESSENGERRESPONSE_STATUS._serialized_end=791
  _DAYNIGHTREQUEST._serialized_start=804
  _DAYNIGHTREQUEST._serialized_end=904
  _DAYNIGHTREQUEST_TIME._serialized_start=878
  _DAYNIGHTREQUEST_TIME._serialized_end=904
  _DAYNIGHTRESPONSE._serialized_start=907
  _DAYNIGHTRESPONSE._serialized_end=1113
  _DAYNIGHTRESPONSE_GAMEOVER._serialized_start=1062
  _DAYNIGHTRESPONSE_GAMEOVER._serialized_end=1113
  _KILLPLAYERREQUEST._serialized_start=1115
  _KILLPLAYERREQUEST._serialized_end=1177
  _KILLPLAYERRESPONSE._serialized_start=1179
  _KILLPLAYERRESPONSE._serialized_end=1199
  _DETECTIVEMOVEREQUEST._serialized_start=1201
  _DETECTIVEMOVEREQUEST._serialized_end=1266
  _DETECTIVEMOVERESPONSE._serialized_start=1268
  _DETECTIVEMOVERESPONSE._serialized_end=1319
  _PUBLISHDATAREQUEST._serialized_start=1321
  _PUBLISHDATAREQUEST._serialized_end=1374
  _PUBLISHDATARESPONSE._serialized_start=1376
  _PUBLISHDATARESPONSE._serialized_end=1397
  _INFOREQUEST._serialized_start=1399
  _INFOREQUEST._serialized_end=1430
  _INFORESPONSE._serialized_start=1432
  _INFORESPONSE._serialized_end=1477
  _MAFIASERVICE._serialized_start=1544
  _MAFIASERVICE._serialized_end=2070
# @@protoc_insertion_point(module_scope)
