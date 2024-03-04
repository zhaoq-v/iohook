{
	"targets": [{
		"target_name": "uiohook",
		"type": "shared_library",
		"sources": [
			"libuiohook/include/uiohook.h",
			"libuiohook/src/logger.c",
			"libuiohook/src/logger.h",
			"libuiohook/src/windows/dispatch_event.h",
			"libuiohook/src/windows/dispatch_event.c",
			"libuiohook/src/windows/input_helper.h",
			"libuiohook/src/windows/input_helper.c",
			"libuiohook/src/windows/input_hook.c",
			"libuiohook/src/windows/post_event.c",
			"libuiohook/src/windows/system_properties.c",
			"libuiohook/src/windows/monitor_helper.h",
			"libuiohook/src/windows/monitor_helper.c"
		],
		"include_dirs": [
			'node_modules/nan',
			'libuiohook/include',
			'libuiohook/src'
		]
	}]
}
