class Motor:
    def __init__(self, id: int, merk: str, model: str, engine_type: str):
        self.id = id
        self.merk = merk
        self.model = model
        self.engine_type = engine_type

    def to_dict(self):
        return {
            "id": self.id,
            "merk": self.merk,
            "model": self.model,
            "engine_type": self.engine_type
        }

    @staticmethod
    def from_dict(data: dict):
        # Pastikan semua key ada
        for key in ("id", "merk", "model", "engine_type"):
            if key not in data:
                raise KeyError(f"Missing key: {key}")

        # Validasi tipe
        if not isinstance(data["id"], int):
            raise TypeError("id must be int")
        if not isinstance(data["merk"], str):
            raise TypeError("merk must be str")
        if not isinstance(data["model"], str):
            raise TypeError("model must be str")
        if not isinstance(data["engine_type"], str):
            raise TypeError("engine_type must be str")

        return Motor(
            id=data["id"],
            merk=data["merk"],
            model=data["model"],
            engine_type=data["engine_type"]
        )
