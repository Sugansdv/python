from models.sender import Sender
from models.receiver import Receiver
from models.parcel import Parcel
from models.tracking import Tracking

def main():
    s1 = Sender("Alice", "New York")
    r1 = Receiver("Bob", "California")
    parcel1 = Parcel(s1, r1, 5.5)

    print("\n Parcel Details:")
    print(parcel1)

    print("\n Is Tracking ID valid?")
    print(Tracking.validate_tracking_id(parcel1.tracking))

if __name__ == "__main__":
    main()
