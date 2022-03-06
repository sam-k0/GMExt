
#define API_Init
API_Define_Styles ();
 
global.external_api_updown_setpos32 = external_define ('Max WinAPI 2.dll','hobbl_com_updown_setpos32',dll_stdcall,ty_real,2,ty_real,ty_real);
global.external_api_updown_setrange = external_define ('Max WinAPI 2.dll','hobbl_com_updown_setrange',dll_stdcall,ty_real,3,ty_real,ty_real,ty_real);
global.external_api_updown_setrange32 = external_define ('Max WinAPI 2.dll','hobbl_com_updown_setrange32',dll_stdcall,ty_real,3,ty_real,ty_real,ty_real);
 
 
#define API_Define_Styles
