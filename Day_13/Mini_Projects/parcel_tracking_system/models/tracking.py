class Tracking:
    tracking_counter = 1000  # class variable

    @staticmethod
    def validate_tracking_id(tracking_id):
        return isinstance(tracking_id, str) and tracking_id.startswith("PKG")

    @classmethod
    def generate_tracking(cls, parcel):
        cls.tracking_counter += 1
        return f"PKG{cls.tracking_counter}"
