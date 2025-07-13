import pandas as pd

# Load the dataset
file_path =  r"D:\MINI PROJECT - 2nd yr (Online food order analysis)\New Delhi -Online food orders data set.csv" # Update the path if necessary
data = pd.read_csv(file_path)

# Step 1: Convert date and time columns to datetime format
data['order_date_time'] = pd.to_datetime(data['Order Date and Time'], format='%d-%m-%Y %H:%M')
data['delivery_date_time'] = pd.to_datetime(data['Delivery Date and Time'], format='%d-%m-%Y %H:%M')

# Step 2: Extract additional features
data['order_day_of_week'] = data['order_date_time'].dt.day_name()
data['delivery_day_of_week'] = data['delivery_date_time'].dt.day_name()
data['order_hour'] = data['order_date_time'].dt.hour
data['delivery_hour'] = data['delivery_date_time'].dt.hour

# Step 3: Clean "Discounts and Offers" column
def clean_discounts(offer):
    if pd.isnull(offer) or offer.lower() == 'none':
        return 'No Discount'
    return offer.strip()

data['discounts_and_offers'] = data['Discounts and Offers'].apply(clean_discounts)

# Step 4: Rename columns for consistency
data.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# Step 5: Drop unnecessary columns if not needed
data.drop(columns=['order_date_and_time', 'delivery_date_and_time'], inplace=True)

# Save the preprocessed dataset
preprocessed_file_path = 'preprocessed_online_food_orders.csv'
data.to_csv(preprocessed_file_path, index=False)

print(f"Preprocessed dataset saved to {preprocessed_file_path}")
