import requests

headers = {
    'host': 'b-graph.facebook.com',
    'x-fb-request-analytics-tags': '{"network_tags":{"product":"256002347743983","request_category":"graphql","purpose":"none","retry_attempt":"0"},"application_tags":"graphservice"}',
    'x-fb-rmd': 'state=URL_ELIGIBLE',
    'priority': 'u=3, i',
    'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 9; ASUS_AI2401_A Build/PQ3A.190705.05150936) [FBAN/Orca-Android;FBAV/537.0.0.52.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/858963017;FBCR/Grameenphone;FBMF/ROG;FBBD/ROG;FBDV/ASUS_AI2401_A;FBSV/9;FBCA/x86_64:arm64-v8a;FBDM/{density=2.0,width=720,height=1280};FB_FW/1;]',
    'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'x-zero-f-device-id': '8ebfc41c-752d-449e-bf2c-ad76ec92671e',
    'x-graphql-client-library': 'graphservice',
    'content-type': 'application/x-www-form-urlencoded',
    'x-zero-eh': '664c0faaac849cb891d0a261fbb72a12',
    'content-encoding': 'gzip',
    'x-fb-net-hni': '47001',
    'x-fb-sim-hni': '47001',
    'authorization': 'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
    'x-zero-state': 'unknown',
    'app-scope-id-header': '8ebfc41c-752d-449e-bf2c-ad76ec92671e',
    'x-fb-connection-type': 'WIFI',
    'x-tigon-is-retry': 'False',
    # 'accept-encoding': 'gzip, deflate',
    'x-fb-http-engine': 'Tigon/Liger',
    'x-fb-client-ip': 'True',
    'x-fb-server-cluster': 'True',
    'x-fb-conn-uuid-client': '4269f9d29ae7aaf0a5978ab8ad3b545f',
}

data = {
    'method': 'post',
    'pretty': 'false',
    'format': 'json',
    'server_timestamps': 'true',
    'locale': 'en_US',
    'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'fb_api_caller_class': 'graphservice',
    'client_doc_id': '119940804211325201326173338565',
    'fb_api_client_context': '{"is_background":false}',
    'variables': '{"params":{"params":"{params:{\\"client_input_params\\":{\\"blocked_uids\\":[],\\"aac\\":\\"{\\\\\\"aac_init_timestamp\\\\\\":1785089156,\\\\\\"aacjid\\\\\\":\\\\\\"d486ee6f-1218-462f-8752-3965df924bb7\\\\\\",\\\\\\"aaccs\\\\\\":\\\\\\"iBI_SzPbNaJwb1-1T4BxH7Qrtvw3JUwLX3Qie7ygmQI\\\\\\"}\\",\\"sim_phones\\":[\\"\\"],\\"aymh_accounts\\":[],\\"network_bssid\\":null,\\"secure_family_device_id\\":\\"ad4dcd0c-c1ce-4319-b451-8fcf3eb3ad9a\\",\\"attestation_result\\":{\\"keyHash\\":\\"0a1a512799700dc845893b5d7c1d2053c59c2ae5f33035df1c82238dc557777c\\",\\"data\\":\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiJLM00vT1gwMkJxdzliQ0wrUE1FU1o0WjFxbDRkVUxsS3pKdDU1ZXgvT3YwPSIsInVzZXJuYW1lIjoiZW1haWxvZW51bWVyIn0=\\",\\"signature\\":\\"MEYCIQDcgnh++NBDlPqrWd207QLim5gLVy//UTTkJ5KQ9gUMPgIhAJ6VtgBkJLibx08R0ePkL/Dggo5szT78YsWMdSHViXS2\\"},\\"has_granted_read_contacts_permissions\\":0,\\"auth_secure_device_id\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"password\\":\\"#PWD_MSGR:2:1785089237:AeGNAKuOQeONJRLe1iIAAUQi6UQHskgblzCWq3pcLaMAFjUfWZ/1TgGHElkDJ/cAItKuQhEuSkJNCacDkaauhwyRUS+bvBMjoECa7ARwpI2PL8PHwzY41SNc7BNaJLf0jqtJdrgyRqcc2RXAV40phxGQNIDyghK+Cx2YNPQPqHNIRxHK5W6af7+DmuE0aDcIrYmGz04VXqZ8dT5+BFUaoTG77aGCbqyFteBL+D0nfgroTQjMZb6RTdUEIipWsCaVVn93H9JnChfJ54RqkIYYNZ7WH+DowziBwL3IWHHFPRx6goUu49zBIqDMQeEJB7fVRdSzNvAUIb/7f2+Y81Z39u+Jv3qelysVPiFuSNOKZinjoQHnsc2H57TFCzAnqOcOs+pzbpPTy20=\\",\\"sso_token_map_json_string\\":\\"\\",\\"block_store_machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"event_flow\\":\\"login_manual\\",\\"password_contains_non_ascii\\":\\"false\\",\\"client_known_key_hash\\":\\"\\",\\"sso_accounts_auth_data\\":[],\\"encrypted_msisdn\\":\\"\\",\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"device_id\\":\\"8ebfc41c-752d-449e-bf2c-ad76ec92671e\\",\\"zero_balance_state\\":\\"\\",\\"login_attempt_count\\":1,\\"machine_id\\":\\"\\",\\"accounts_list\\":[],\\"gms_incoming_call_retriever_eligibility\\":\\"client_not_supported\\",\\"family_device_id\\":\\"8ebfc41c-752d-449e-bf2c-ad76ec92671e\\",\\"fb_ig_device_id\\":[],\\"device_emails\\":[],\\"try_num\\":1,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"event_step\\":\\"home_page\\",\\"headers_infra_flow_id\\":\\"\\",\\"openid_tokens\\":{},\\"contact_point\\":\\"emailoenumer\\"},\\"server_params\\":{\\"should_trigger_override_login_2fa_action\\":0,\\"is_from_logged_out\\":0,\\"should_trigger_override_login_success_action\\":0,\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"waterfall_id\\":\\"74713eca-fc10-4d50-b3e3-a4eb68a96c19\\",\\"two_step_login_type\\":\\"one_step_login\\",\\"login_source\\":\\"Login\\",\\"is_platform_login\\":0,\\"pw_encryption_try_count\\":1,\\"login_entry_point\\":\\"logged_out\\",\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"is_from_aymh\\":0,\\"offline_experiment_group\\":\\"caa_iteration_v3_perf_msg_6\\",\\"is_from_landing_page\\":0,\\"left_nav_button_action\\":\\"NONE\\",\\"password_text_input_id\\":\\"3zshr2:103\\",\\"is_from_empty_password\\":0,\\"is_from_msplit_fallback\\":0,\\"ar_event_source\\":\\"login_home_page\\",\\"username_text_input_id\\":\\"3zshr2:102\\",\\"layered_homepage_experiment_group\\":null,\\"device_id\\":\\"8ebfc41c-752d-449e-bf2c-ad76ec92671e\\",\\"login_surface\\":\\"login_home\\",\\"INTERNAL__latency_qpl_instance_id\\":24151446200559,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"is_caa_perf_enabled\\":1,\\"credential_type\\":\\"password\\",\\"is_from_password_entry_page\\":0,\\"caller\\":\\"gslr\\",\\"family_device_id\\":\\"8ebfc41c-752d-449e-bf2c-ad76ec92671e\\",\\"is_from_assistive_id\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\",\\"is_from_logged_in_switcher\\":0}},}","bloks_versioning_id":"22848619271d7ad4c7876f2d77349529dbeb6d0d3dda6ebe5f18955c5376b89c","app_id":"com.bloks.www.bloks.caa.login.async.send_login_request"},"scale":"2","nt_context":{"is_flipper_enabled":false,"theme_params":[{"value":[],"design_system_name":"FDS"}],"debug_tooling_metadata_token":null}}',
    'fb_api_analytics_tags': '["GraphServices"]',
    'client_trace_id': '9b3f0ff3-3a04-45b1-8044-f31b0ebced5d',
}

response = requests.post('https://b-graph.facebook.com/graphql', headers=headers, data=data)