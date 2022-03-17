# SessionsResponseInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_type** | **str** | Agent type - SERVER or CLIENT | [optional] 
**name** | **str** | Agent name | [optional] 
**session_name** | **str** | Mnemonic FIX session name - SenderId:SubId-&gt;AcceptorId:SubId | [optional] 
**initiator** | **str** | FIX session initiator id | [optional] 
**initiator_sub** | **str** | FIX session initiator sub id | [optional] 
**acceptor** | **str** | FIX session acceptor id | [optional] 
**acceptor_sub** | **str** | FIX session acceptor sub id | [optional] 
**time_updated** | **int** | Unix time since Session status was updated | [optional] 
**last_sent** | **int** | FIX session last sent sequence number | [optional] 
**last_received** | **int** | FIX session last received sequence number | [optional] 
**state** | **str** | FIX session status | [optional] 
**trading_halted** | **bool** | Session trading status | [optional] 
**short_sale_prohibited** | **bool** | Session short sale status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

