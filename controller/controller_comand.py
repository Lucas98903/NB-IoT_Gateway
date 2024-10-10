from services.preference.configuration import equipmentConfiguration


class managerCommand():

    def managerCommand(preferences):
        configuration = equipmentConfiguration()
        codes = []
        out_of_range = []

        if preferences.upload_time:
            code  = configuration.set_upload_time(preferences.upload_time)
            if code:
                codes.append(code)
            else:
                out_of_range.append({'upload_time': f"Value: {preferences.upload_time} - out of range time in hour 01~168 (h)"})
        
        if preferences.height_threshold:
            code  = configuration.set_height_Threshold(preferences.height_threshold)
            if code:
                codes.append(code)
            else:
                out_of_range.append({"height_threshold": f"Value: {preferences.height_threshold} - out of range 5-255 (cm)"})

        if preferences.alarmBattery:
            code  = configuration.set_height_Threshold(preferences.alarmBattery)
            if code:
                codes.append(code)
            else:
                out_of_range.append({"alarmBattery": f"Value: {preferences.alarmBattery} -out of range level in percentual 5-99 (%)"})

        if preferences.cycle_detection:
            code  = configuration.set_height_Threshold(preferences.set_cycle_detection)
            if code:
                codes.append(code)
            else:
                out_of_range.append({"cycle_detection": f"Value: {preferences.set_cycle_detection} -out of range time in minute 01-60 (min)"})
        
        if preferences.magnetic_threshold:
            code  = configuration.set_magnetic_threshold(preferences.magnetic_threshold)
            if code:
                codes.append(code)
            else:
                out_of_range.append({"magnetic_threshold": f"Value: {preferences.magnetic_threshold} -out of range magnetic in Gauss 00001 - 655535"})

        if preferences.restart_sensor != None:
            code  = configuration.restart_sensor()
            codes.append(code)

        if preferences.action_serial != None:
            if preferences.action_serial:
                code  = configuration.open_serial()
            else:
                code  = configuration.close_serial()

            codes.append(code)

        if preferences.action_bluetooth != None:
            if preferences.action_bluetooth:
                code  = configuration.open_bluetooth()
            else:
                code  = configuration.close_bluetooth()
                
            codes.append(code)
        
        return codes, out_of_range
    

