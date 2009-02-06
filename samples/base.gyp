{
  'variables': {
    'depth': '..',
  },
  'includes': [
    '../build/common.gypi',
  ],
  'target_defaults': {
    'include_dirs': [
      '..',
    ],
  },
  'targets': [
    {
      'target_name': 'base',
      'type': 'static_library',
      'dependencies': [
        '../third_party/icu38/icu38.gyp:icui18n',
        '../third_party/icu38/icu38.gyp:icuuc',
      ],
      'sources': [
        '../build/build_config.h',
        'third_party/dmg_fp/dtoa.cc',
        'third_party/dmg_fp/g_fmt.cc',
        'third_party/nspr/prtime.cc',
        'third_party/nss/sha512.cc',
        'atomicops_internals_x86_gcc.cc',
        'at_exit.cc',
        'at_exit.h',
        'atomic_ref_count.h',
        'atomic_sequence_num.h',
        'atomicops.h',
        'atomicops_internals_x86_msvc.h',
        'base_drag_source.cc',
        'base_drag_source.h',
        'base_drop_target.cc',
        'base_drop_target.h',
        'base_paths.cc',
        'base_paths.h',
        'base_paths_linux.cc',
        'base_paths_mac.mm',
        'base_paths_win.cc',
        'base_paths_win.h',
        'base_switches.cc',
        'base_switches.h',
        'basictypes.h',
        'bzip2_error_handler.cc',
        'clipboard.cc',
        'clipboard.h',
        'clipboard_linux.cc',
        'clipboard_mac.mm',
        'clipboard_util.cc',
        'clipboard_util.h',
        'clipboard_win.cc',
        'command_line.cc',
        'command_line.h',
        'compiler_specific.h',
        'condition_variable.h',
        'condition_variable_posix.cc',
        'condition_variable_win.cc',
        'cpu.cc',
        'cpu.h',
        'data_pack.cc',
        'debug_on_start.cc',
        'debug_on_start.h',
        'debug_util.cc',
        'debug_util.h',
        'debug_util_posix.cc',
        'debug_util_win.cc',
        'directory_watcher.h',
        'directory_watcher_win.cc',
        'event_recorder.cc',
        'event_recorder.h',
        'event_recorder_stubs.cc',
        'field_trial.cc',
        'field_trial.h',
        'file_path.cc',
        'file_path.h',
        'file_util.cc',
        'file_util.h',
        'file_util_linux.cc',
        'file_util_mac.mm',
        'file_util_posix.cc',
        'file_util_win.cc',
        'file_version_info.cc',
        'file_version_info.h',
        'file_version_info_linux.cc',
        'file_version_info_mac.mm',
        'fix_wp64.h',
        'float_util.h',
        'hash_tables.h',
        'histogram.cc',
        'histogram.h',
        'hmac.h',
        'hmac_mac.cc',
        'hmac_nss.cc',
        'hmac_win.cc',
        'iat_patch.cc',
        'iat_patch.h',
        'icu_util.cc',
        'icu_util.h',
        'id_map.h',
        'idle_timer.cc',
        'idle_timer.h',
        'idle_timer_none.cc',
        'image_util.cc',
        'image_util.h',
        'json_reader.cc',
        'json_reader.h',
        'json_writer.cc',
        'json_writer.h',
        'keyboard_codes.h',
        'keyboard_codes_win.h',
        'lazy_instance.cc',
        'lazy_instance.h',
        'linked_ptr.h',
        'lock.cc',
        'lock.h',
        'lock_impl.h',
        'lock_impl_posix.cc',
        'lock_impl_win.cc',
        'logging.cc',
        'logging.h',
        'mac_util.mm',
        'md5.cc',
        'md5.h',
        'memory_debug.cc',
        'memory_debug.h',
        'message_loop.cc',
        'message_loop.h',
        'message_pump.h',
        'message_pump_default.cc',
        'message_pump_default.h',
        'message_pump_glib.cc',
        'message_pump_libevent.cc',
        'message_pump_mac.mm',
        'message_pump_win.cc',
        'message_pump_win.h',
        'non_thread_safe.cc',
        'non_thread_safe.h',
        'nss_init.cc',
        'object_watcher.cc',
        'object_watcher.h',
        'observer_list.h',
        'observer_list_threadsafe.h',
        'path_service.cc',
        'path_service.h',
        'pe_image.cc',
        'pe_image.h',
        'pickle.cc',
        'pickle.h',
        'platform_file.h',
        'platform_file_win.cc',
        'platform_file_posix.cc',
        'platform_thread.h',
        'platform_thread_mac.mm',
        'platform_thread_posix.cc',
        'platform_thread_win.cc',
        'port.h',
        'process.h',
        'process_posix.cc',
        'process_util.h',
        'process_util_linux.cc',
        'process_util_mac.mm',
        'process_util_posix.cc',
        'process_util_win.cc',
        'process_win.cc',
        'rand_util.cc',
        'rand_util_posix.cc',
        'rand_util_win.cc',
        'ref_counted.cc',
        'ref_counted.h',
        'registry.cc',
        'registry.h',
        'resource_util.cc',
        'resource_util.h',
        'revocable_store.cc',
        'revocable_store.h',
        'scoped_bstr_win.cc',
        'scoped_bstr_win.h',
        'scoped_clipboard_writer.cc',
        'scoped_clipboard_writer.h',
        'scoped_comptr_win.h',
        'scoped_handle.h',
        'scoped_nsautorelease_pool.h',
        'scoped_nsautorelease_pool.mm',
        'scoped_ptr.h',
        'scoped_temp_dir.cc',
        'scoped_temp_dir.h',
        'sha2.cc',
        'sha2.h',
        'shared_memory.h',
        'shared_memory_posix.cc',
        'shared_memory_win.cc',
        'simple_thread.cc',
        'simple_thread.h',
        'singleton.h',
        'spin_wait.h',
        'stack_container.h',
        'stats_counters.h',
        'stats_table.cc',
        'stats_table.h',
        'string16.cc',
        'string16.h',
        'string_escape.cc',
        'string_escape.h',
        'string_piece.cc',
        'string_piece.h',
        'string_tokenizer.h',
        'string_util.cc',
        'string_util.h',
        'string_util_icu.cc',
        'string_util_win.h',
        'sys_info.h',
        'sys_info_posix.cc',
        'sys_info_win.cc',
        'sys_string_conversions.h',
        'sys_string_conversions_linux.cc',
        'sys_string_conversions_mac.mm',
        'sys_string_conversions_win.cc',
        'system_monitor.cc',
        'system_monitor.h',
        'system_monitor_posix.cc',
        'system_monitor_win.cc',
        'task.h',
        'test_file_util.h',
        'test_file_util_linux.cc',
        'test_file_util_mac.cc',
        'test_file_util_win.cc',
        'thread.cc',
        'thread.h',
        'thread_collision_warner.cc',
        'thread_collision_warner.h',
        'thread_local.h',
        'thread_local_posix.cc',
        'thread_local_storage.h',
        'thread_local_storage_posix.cc',
        'thread_local_storage_win.cc',
        'thread_local_win.cc',
        'time.cc',
        'time.h',
        'time_format.cc',
        'time_format.h',
        'time_mac.cc',
        'time_posix.cc',
        'time_win.cc',
        'timer.cc',
        'timer.h',
        'trace_event.cc',
        'trace_event.h',
        'tracked.cc',
        'tracked.h',
        'tracked_objects.cc',
        'tracked_objects.h',
        'tuple.h',
        'values.cc',
        'values.h',
        'version.cc',
        'version.h',
        'waitable_event.h',
        'waitable_event_posix.cc',
        'waitable_event_watcher.h',
        'waitable_event_watcher_posix.cc',
        'waitable_event_watcher_win.cc',
        'waitable_event_win.cc',
        'watchdog.cc',
        'watchdog.h',
        'win_util.cc',
        'win_util.h',
        'windows_message_list.h',
        'wmi_util.cc',
        'wmi_util.h',
        'word_iterator.cc',
        'word_iterator.h',
        'worker_pool.cc',
        'worker_pool.h',
        'worker_pool_mac.mm',
      ],
      # These warnings are needed for the files in third_party\dmg_fp.
      'msvs_disabled_warnings': [
        4244, 4554, 4018, 4102,
      ],
      'conditions': [
        [ 'OS == "linux"', {
            'sources/': [ ['exclude', '_(mac|win)\\.cc$'],
                          ['exclude', '\\.mm?$' ] ],
            'sources!': [
              # Linux has an implementation of idle_timer that depends
              # on XScreenSaver, but it's unclear if we want it yet,
              # so use idle_timer_none.cc instead.
              'idle_timer.cc',
            ],
            'cflags': ['-Wno-write-strings'],
          },
          {  # else: OS != "linux"
            'sources!': [
              'atomicops_internals_x86_gcc.cc',
              'data_pack.cc',
              'hmac_nss.cc',
              'idle_timer_none.cc',
              'message_pump_glib.cc',
              'nss_init.cc',
              'time_posix.cc',
            ],
          }
        ],
        [ 'OS == "mac"', {
            'sources/': [ ['exclude', '_(linux|win)\\.cc$'] ],
            'sources!': [
              'worker_pool.cc',
            ],
            'link_settings': {
              'libraries': [
                '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
                '$(SDKROOT)/System/Library/Frameworks/Carbon.framework',
                '$(SDKROOT)/System/Library/Frameworks/CoreFoundation.framework',
                '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
              ],
            },
          },
        ],
        [ 'OS == "win"', {
            'sources/': [ ['exclude', '_(linux|mac|posix)\\.cc$'],
                          ['exclude', '\\.mm?$' ] ],
            'sources!': [
              'message_pump_libevent.cc',
              'string16.cc',
            ],
          },
          {  # else: OS != "win"
            'dependencies': ['../third_party/libevent/libevent.gyp:libevent'],
            'sources!': [
              'base_drag_source.cc',
              'base_drop_target.cc',
              'cpu.cc',
              'clipboard_util.cc',
              'debug_on_start.cc',
              'event_recorder.cc',
              'file_version_info.cc',
              'iat_patch.cc',
              'image_util.cc',
              'object_watcher.cc',
              'pe_image.cc',
              'registry.cc',
              'resource_util.cc',
              'win_util.cc',
              'wmi_util.cc',
            ],
          },
        ],
      ],
    },
    {
      'target_name': 'base_gfx',
      'type': 'static_library',
      'sources': [
        'gfx/gdi_util.cc',
        'gfx/gdi_util.h',
        'gfx/jpeg_codec.cc',
        'gfx/jpeg_codec.h',
        'gfx/native_theme.cc',
        'gfx/native_theme.h',
        'gfx/native_widget_types.h',
        'gfx/platform_canvas.h',
        'gfx/platform_canvas_linux.h',
        'gfx/platform_canvas_mac.h',
        'gfx/platform_device_linux.h',
        'gfx/platform_device_mac.h',
        'gfx/png_decoder.cc',
        'gfx/png_decoder.h',
        'gfx/png_encoder.cc',
        'gfx/png_encoder.h',
        'gfx/point.cc',
        'gfx/point.h',
        'gfx/rect.cc',
        'gfx/rect.h',
        'gfx/size.cc',
        'gfx/size.h',
      ],
      'xcode_framework_dirs': [
        '$(SDKROOT)/System/Library/Frameworks/ApplicationServices.framework/Frameworks',
      ],
      'dependencies': [
        'base',
        '../skia/skia.gyp:skia',
        '../third_party/libjpeg/libjpeg.gyp:libjpeg',
        '../third_party/libpng/libpng.gyp:libpng',
      ],
      'conditions': [
        [ 'OS != "win"', { 'sources!': [
          'gfx/gdi_util.cc',
          'gfx/native_theme.cc' ]
        }],
      ],
    },
    {
      'target_name': 'base_unittests',
      'type': 'executable',
      'sources': [
        'gfx/jpeg_codec_unittest.cc',
        'gfx/native_theme_unittest.cc',
        'gfx/png_codec_unittest.cc',
        'gfx/rect_unittest.cc',
        'at_exit_unittest.cc',
        'atomicops_unittest.cc',
        'clipboard_unittest.cc',
        'command_line_unittest.cc',
        'condition_variable_unittest.cc',
        'data_pack_unittest.cc',
        'directory_watcher_unittest.cc',
        'field_trial_unittest.cc',
        'file_path_unittest.cc',
        'file_util_unittest.cc',
        'file_version_info_unittest.cc',
        'histogram_unittest.cc',
        'hmac_unittest.cc',
        'idletimer_unittest.cc',
        'json_reader_unittest.cc',
        'json_writer_unittest.cc',
        'lazy_instance_unittest.cc',
        'linked_ptr_unittest.cc',
        'mac_util_unittest.cc',
        'message_loop_unittest.cc',
        'object_watcher_unittest.cc',
        'observer_list_unittest.cc',
        'path_service_unittest.cc',
        'pe_image_unittest.cc',
        'pickle_unittest.cc',
        'pr_time_unittest.cc',
        'process_util_unittest.cc',
        'rand_util_unittest.cc',
        'ref_counted_unittest.cc',
        'run_all_unittests.cc',
        'scoped_bstr_win_unittest.cc',
        'scoped_comptr_win_unittest.cc',
        'scoped_ptr_unittest.cc',
        'sha2_unittest.cc',
        'shared_memory_unittest.cc',
        'simple_thread_unittest.cc',
        'singleton_unittest.cc',
        'stack_container_unittest.cc',
        'stats_table_unittest.cc',
        'string_escape_unittest.cc',
        'string_piece_unittest.cc',
        'string_tokenizer_unittest.cc',
        'string_util_unittest.cc',
        'sys_info_unittest.cc',
        'sys_string_conversions_unittest.cc',
        'sys_string_conversions_unittest.cc',
        'system_monitor_unittest.cc',
        'thread_collision_warner_unittest.cc',
        'thread_local_storage_unittest.cc',
        'thread_local_unittest.cc',
        'thread_unittest.cc',
        'time_unittest.cc',
        'time_win_unittest.cc',
        'timer_unittest.cc',
        'tracked_objects_unittest.cc',
        'tuple_unittest.cc',
        'values_unittest.cc',
        'waitable_event_unittest.cc',
        'watchdog_unittest.cc',
        'win_util_unittest.cc',
        'wmi_util_unittest.cc',
        'word_iterator_unittest.cc',
        'worker_pool_unittest.cc',
      ],
      'include_dirs': [
        # word_iterator.h (used by word_iterator_unittest.cc) leaks an ICU
        # #include for unicode/uchar.h.  This should probably be cleaned up.
        '../third_party/icu38/public/common',
      ],
      'dependencies': [
        'base',
        'base_gfx',
        '../testing/gtest.gyp:gtest',
      ],
      'conditions': [
        [ 'OS == "linux"', {
            'sources!': [
              'file_version_info_unittest.cc',
              # Linux has an implementation of idle_timer, but it's unclear
              # if we want it yet, so leave it 'unported' for now.
              'idletimer_unittest.cc',
            ],
          },
          { # OS != "linux"
            'sources!': [
              'data_pack_unittest.cc',
            ],
          },
        ],
        [ 'OS == "mac"', {
            'sources!': [
              'stats_table_unittest.cc',
            ],
          },
          { # OS != "mac"
            'sources!': [
              'mac_util_unittest.cc',
            ],
          },
        ],
        # This is needed to trigger the dll copy step on windows.
        # TODO(mark): This should not be necessary.
        [ 'OS == "win"', {
            'dependencies': [
              '../third_party/icu38/icu38.gyp:icudata',
            ],
          },
          {  # OS != "win", {
            'sources!': [
              'gfx/native_theme_unittest.cc',
              'directory_watcher_unittest.cc',
              'object_watcher_unittest.cc',
              'pe_image_unittest.cc',
              'scoped_bstr_win_unittest.cc',
              'scoped_comptr_win_unittest.cc',
              'system_monitor_unittest.cc',
              'sys_string_conversions_unittest.cc',
              'time_win_unittest.cc',
              'win_util_unittest.cc',
              'wmi_util_unittest.cc',
            ],
          }
        ],
      ],
    },
  ],
}
