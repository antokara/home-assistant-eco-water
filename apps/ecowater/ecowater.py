import mqttapi as mqtt

class EcoWater(mqtt.Mqtt):
    def initialize(self):
        self.run_every(self.run_fn, datetime.datetime.now() + timedelta(seconds=3), 1 * 60)
	

    def run_fn(self, kwargs):
        self.mqtt_publish('ecowater/test', 5)