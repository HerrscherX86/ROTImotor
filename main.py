from data.motor_repository_json import MotorRepositoryJSON
from use_cases.motor_use_case import MotorUseCase
from interface.cli import show_menu

def main():
    repo = MotorRepositoryJSON("data/storage/motors.json")
    use_case = MotorUseCase(repo)

    while True:
        show_menu()
        choice = input("Pilih: ")
        try:
            if choice == "1":
                motors = use_case.list_motors()
                for m in motors:
                    print(m.to_dict())
            elif choice == "2":
                id = int(input("ID: "))
                motor = use_case.get_motor(id)
                print(motor.to_dict())
            elif choice == "3":
                id = int(input("ID: "))
                merk = input("Merek: ")
                model = input("Model: ")
                eng = input("Engine Type: ")
                use_case.create_motor(id, merk, model, eng)
            elif choice == "4":
                id = int(input("ID: "))
                merk = input("Merek: ")
                model = input("Model: ")
                eng = input("Engine Type: ")
                use_case.update_motor(id, merk, model, eng)
            elif choice == "5":
                id = int(input("ID: "))
                use_case.delete_motor(id)
            elif choice == "6":
                break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
