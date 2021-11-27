import botocore
import boto3
import json
from typing import Dict, List
from data.Image import Image
from data.Region import Region
from data.Reservation import Reservation

if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    regions_response = response['Regions']

    regions: List[Region] = []
    for region in regions_response:
        try:
            regions.append(Region.Schema().load(region))
        except Exception as err:
            print(err)
            continue

    region_to_reservations: Dict[Region, List[Reservation]] = {}
    for region in regions:
        try:
            print("Connecting to:", region.RegionName)
            client = boto3.client('ec2', region.RegionName)
            response = client.describe_instances()
            region_to_reservations[region] = []
            reservations_response = response['Reservations']
            for reservation in reservations_response:
                region_to_reservations[region].append(Reservation.Schema().loads(json.dumps(reservation, indent=4, sort_keys=True, default=str)))
                print("Data received")
        except botocore.exceptions.ClientError:
            print("Unauthorized")
            continue
        except Exception as err:
            print(err)

    region_to_images: Dict[Region, Dict[str, Image]] = {}
    for region in region_to_reservations.keys():
        client = boto3.client('ec2', region.RegionName)
        # get all images id that in the current region for a single query to the api
        images_ids = []
        for reservation in region_to_reservations[region]:
            for instance in reservation.Instances:
                images_ids.append(instance.ImageId)
        try:
            # send a request with all the known ids
            response = client.describe_images(ImageIds=[','.join(image_id for image_id in images_ids)])
            region_to_images[region] = {}
            images_response = response['Images']
            for image_res in images_response:
                # deserialize each id and save it
                image = Image.Schema().loads(json.dumps(image_res, indent=4, sort_keys=True, default=str))
                region_to_images[region][image.ImageId] = image
        except botocore.exceptions.ClientError:
            print("Unauthorized")
            continue
        except Exception as err:
            print(err)




