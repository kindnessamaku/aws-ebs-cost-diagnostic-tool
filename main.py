import boto3
from datetime import datetime, timezone

AGE_THRESHOLD = 30  # Days
GB_COST_ESTIMATE = 0.08  # Avg cost for gp3

ec2 = boto3.client("ec2")

def create_snapshot(volume_id):
    """Creates a safety backup before marking for cleanup."""
    try:
        response = ec2.create_snapshot(
            VolumeId=volume_id,
            Description=f"Automated snapshot before cleanup - Volume {volume_id}"
        )
        return response["SnapshotId"]
    except Exception as e:
        print(f"❌ Error creating snapshot for {volume_id}: {e}")
        return None

def get_unattached_volumes():
    """Fetches unattached volumes and calculates age/cost."""
    
    response = ec2.describe_volumes(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )
    
    volumes = response.get("Volumes", [])
    unattached_report = []

    for volume in volumes:
        v_id = volume["VolumeId"]
        size = volume["Size"]
        create_time = volume["CreateTime"]

        # Calculate metrics
        age_days = (datetime.now(timezone.utc) - create_time).days
        estimated_cost = size * GB_COST_ESTIMATE

        unattached_report.append({
            "VolumeId": v_id,
            "Size": size,
            "AgeDays": age_days,
            "EstimatedCost": round(estimated_cost, 2),
            "NeedsReview": age_days > AGE_THRESHOLD
        })

    return unattached_report

def main():
    print(f"--- AWS EBS Cost Diagnostic Tool ---")
    volumes = get_unattached_volumes()

    if not volumes:
        print("✅ No unattached EBS volumes found. Your account is clean!")
        return

    total_cost = 0
    created_snapshots = []

    for v in volumes:
        print(f"\nVolume ID: {v['VolumeId']}")
        print(f"Size: {v['Size']} GB | Age: {v['AgeDays']} days")
        print(f"Monthly Waste: ${v['EstimatedCost']}")

        if v["NeedsReview"]:
            print(f"⚠  CRITICAL: Volume exceeds {AGE_THRESHOLD} days.")
            print(f"📸 Action: Creating safety snapshot...")
            
            snap_id = create_snapshot(v["VolumeId"])
            if snap_id:
                created_snapshots.append(snap_id)
                print(f"Successfully created: {snap_id}")

        total_cost += v["EstimatedCost"]
        print("-" * 0)

    # Final Summary Report
    print(f"\n{'='*40}")
    print(f"FINANCIAL SUMMARY")
    print(f"{'='*40}")
    print(f"Total Volumes Flagged: {len(volumes)}")
    print(f"Total Monthly Savings: ${round(total_cost, 2)}")
    
    if created_snapshots:
        print(f"\nSafety Snapshots Created Today:")
        for sid in created_snapshots:
            print(f"- {sid}")
    print(f"{'='*40}")

if __name__ == "__main__":
    main()