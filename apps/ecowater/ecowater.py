import mqttapi as mqtt

class EcoWater(mqtt.Mqtt):
    def initialize(self):
        # Create a time object for 7pm
        time = datetime.time(19, 00, 0)
        # Schedule a daily callback that will call run_daily() at 7pm every night
        self.run_daily(self.run_fn, time)

    def run_fn(self, kwargs):
        self.mqtt_publish('ecowater/test', 5)