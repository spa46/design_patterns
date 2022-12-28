from Logistics import Logistics
from RoadLogistics import RoadLogistics
from ShipLogistics import ShipLogistics


def transport(logistics: Logistics) -> None:
  logistics.createTransport()


if __name__ == "__main__":
  transport(RoadLogistics())
  print("=====")
  transport(ShipLogistics())