CREATE TABLE items (item_name VARCHAR(30),manufacturer_name VARCHAR(30),cost VARCHAR(30),weight INT);
ALTER TABLE items ADD CONSTRAINT pk_constrain PRIMARY KEY (item_name, manufacturer_name)
CREATE TABLE transaction (membership_id VARCHAR(30), item_bought VARCHAR(30), price FLOAT(8),weight INT);
INSERT INTO items (item_name, manufacturer_name, cost, weight) VALUES
('Vapor T-Shirt', 'Karma Apparel', '24.99', 120),
('Retro Sneakers', 'Vintage Kicks', '79.99', 500),
('Organic Superfood Mix', 'Green Guru', '29.99', 300),
('Minimalist Phone Case', 'Sleek Style Co.', '14.99', 50),
('Leather Laptop Bag', 'The Executive', '149.99', 800),
('Bluetooth Earbuds', 'Urban Sound', '69.99', 25),
('Raw Denim Jeans', 'Indigo Society', '99.99', 250),
('Handmade Leather Wallet', 'Artisan Goods', '39.99', 20),
('Sustainable Bamboo Sunglasses', 'EcoWear', '49.99', 30),
('Minimalist Watch', 'Timeless Design', '89.99', 75),
('Organic Cotton Hoodie', 'Green Threads', '59.99', 200),
('Recycled Plastic Water Bottle', 'ReUse', '19.99', 10),
('Electric Scooter', 'Urban Mobility', '399.99', 1500),
('Upcycled Messenger Bag', 'Second Chance', '59.99', 300),
('Hydroponic Herb Garden', 'Green Thumb Co.', '79.99', 40),
('Vintage Sunglasses', 'Retro Specs', '39.99', 20),
('Smart Thermostat', 'EcoTech', '129.99', 50),
('Reusable Grocery Bag Set', 'EcoBags', '24.99', 5),
('Organic Cotton Face Mask', 'Pure Breath', '9.99', 5),
('Smartphone Projector', 'Big Screen', '49.99', 100),
('Wireless Charging Pad', 'Power Up', '29.99', 10),
('Handmade Ceramic Mug', 'Artisan Pottery', '19.99', 5),
('Rustic Wooden Coasters', 'Farmhouse Finds', '14.99', 5),
('Natural Soy Candle', 'Scented Bliss', '29.99', 10),
('Eco-Friendly Yoga Mat', 'Om Gear', '49.99', 100),
('Bamboo Cutting Board', 'Kitchen Essentials', '34.99', 15),
('Handmade Soap Set', 'Clean Beauty', '29.99', 5),
('Reusable Beeswax Wraps', 'Bee Sustainable', '19.99', 5),
('Stainless Steel Water Bottle', 'Hydrate & Co.', '24.99', 5),
('Handwoven Throw Blanket', 'Cozy Home', '89.99', 10),
('Sustainable Running Shoes', 'EcoRun', '129.99', 400),
('Bamboo Toothbrush Set', 'EcoDent', '14.99', 5),
('Organic Cotton Bath Towel Set', 'Green Living', '39.99', 10),
('Portable Solar Charger', 'EcoCharge', '69.99', 200),
('Recycled Glass Water Bottle', 'Pure Glass', '29.99', 10),
('Natural Wood Desk Organizer', 'Rustic Office', '24.99', 5);
INSERT INTO items (item_name, manufacturer_name, cost, weight) VALUES
('Orange Juice', 'Treehouse Beverages', '2.99', 64),
('Paper Towels', 'UltraClean Solutions', '1.50', 32),
('Laptop Charger', 'Tech Accessories Inc', '35.99', 500),
('Sneakers', 'Fit & Fabulous Footwear', '79.99', 1000),
('Bluetooth Speaker', 'SoundSense', '39.99', 300),
('Wireless Earbuds', 'AudioX', '89.99', 45),
('Sweater', 'WinterWear Co.', '49.99', 400),
('Mittens', 'ColdHands Inc.', '12.99', 20),
('Sports Water Bottle', 'HydrateMe', '8.99', 16),
('Running Shoes', 'StrideStrong', '129.99', 750),
('Smart Watch', 'TechWearables', '199.99', 80),
('Gym Bag', 'WorkoutWear', '24.99', 200),
('Hiking Boots', 'TrailBlaze', '89.99', 900),
('Baseball Hat', 'Headgear HQ', '19.99', 8),
('Yoga Mat', 'Om Fitness', '29.99', 120),
('Hair Brush', 'SleekTresses', '6.99', 4),
('Sunglasses', 'SunSmart', '49.99', 12),
('Beach Towel', 'Sun & Sand Co.', '14.99', 30),
('Sunscreen', 'SunShield', '12.99', 8),
('Waterproof Phone Case', 'Aquapac', '24.99', 2),
('Winter Coat', 'ChillOutwear', '149.99', 1200),
('Umbrella', 'RainyDay Gear', '9.99', 16),
('Backpack', 'PackMate', '49.99', 480),
('Travel Pillow', 'SleepOnIt', '19.99', 8),
('Earplugs', 'Silent Nights', '4.99', 1),
('Sleep Mask', 'Darkness Please', '6.99', 1),
('Mouthwash', 'Minty Fresh', '4.99', 16),
('Toothbrush', 'Clean Teeth Co.', '2.99', 4),
('Deodorant', 'FreshScent', '5.99', 8),
('Shampoo', 'SilkyLocks', '8.99', 16),
('Conditioner', 'SmoothStrands', '8.99', 16),
('Bar Soap', 'CleanseMe', '1.99', 2),
('Body Wash', 'LatherUp', '6.99', 8),
('Hand Sanitizer', 'GermAway', '3.99', 1),
('Antibacterial Wipes', 'CleanSurfaces', '7.99', 1),
('Nail Clippers', 'TrimTime', '3.99', 1),
('Tweezers', 'PluckIt', '2.99', 1),
('Razor', 'SharpShave', '9.99', 1),
('Shaving Cream', 'SmoothShave', '5.99', 4);


INSERT INTO transaction (membership_id, item_bought, price, weight)
VALUES
('3c3a1f5b', 'Vapor T-Shirt', '24.99', 120),
('cc82b7e2', 'Retro Sneakers', '79.99', 500),
('ec5aa5d5', 'Organic Superfood Mix', '29.99', 300),
('cc82b7e2', 'Minimalist Phone Case', '14.99', 50),
('3c3a1f5b', 'Leather Laptop Bag', '149.99', 800),
('d3f2c1e7', 'Bluetooth Earbuds', '69.99', 25),
('7e6f8d1a', 'Raw Denim Jeans', '99.99', 250),
('f6e9c3b9', 'Handmade Leather Wallet', '39.99', 20),
('3c3a1f5b', 'Sustainable Bamboo Sunglasses', '49.99', 30),
('d3f2c1e7', 'Minimalist Watch', '89.99', 75),
('cc82b7e2', 'Organic Cotton Hoodie', '59.99', 200),
('7e6f8d1a', 'Recycled Plastic Water Bottle', '19.99', 10),
('3c3a1f5b', 'Electric Scooter', '399.99', 1500),
('d3f2c1e7', 'Upcycled Messenger Bag', '59.99', 300),
('ec5aa5d5', 'Hydroponic Herb Garden', '79.99', 40),
('f6e9c3b9', 'Vintage Sunglasses', '39.99', 20),
('cc82b7e2', 'Smart Thermostat', '129.99', 50),
('3c3a1f5b', 'Reusable Grocery Bag Set', '24.99', 5),
('d3f2c1e7', 'Organic Cotton Face Mask', '9.99', 5),
('7e6f8d1a', 'Smartphone Projector', '49.99', 100),
('cc82b7e2', 'Wireless Charging Pad', '29.99', 10),
('ec5aa5d5', 'Handmade Ceramic Mug', '19.99', 5),
('f6e9c3b9', 'Rustic Wooden Coasters', '14.99', 5),
('3c3a1f5b', 'Natural Soy Candle', '29.99', 10),
('d3f2c1e7', 'Eco-Friendly Yoga Mat', '49.99', 100),
('cc82b7e2', 'Bamboo Cutting Board', '34.99', 15),
('7e6f8d1a', 'Handmade Soap Set', '29.99', 5),
('ec5aa5d5', 'Reusable Beeswax Wraps', '19.99', 5),
('f6e9c3b9', 'Stainless Steel Water Bottle', '24.99', 5);


INSERT INTO transaction (membership_id, item_bought, price, weight) VALUES ('7c08d2', 'Vapor T-Shirt', '24.99', 120);
INSERT INTO transaction (membership_id, item_bought, price, weight) VALUES ('3a12f8', 'Leather Laptop Bag', '149.99', 800);
INSERT INTO transaction (membership_id, item_bought, price, weight) VALUES ('bb34e1', 'Smartphone Projector', '49.99', 100);
INSERT INTO transaction (membership_id, item_bought, price, weight) VALUES ('0c78d1', 'Recycled Glass Water Bottle', '29.99', 10);
INSERT INTO transaction (membership_id, item_bought, price, weight) VALUES ('df32a1', 'Organic Superfood Mix', '29.99', 300);

INSERT INTO transaction (membership_id, item_bought, price, weight) VALUES
('ff2a4c', 'Vintage Sunglasses', '39.99', 20),
('c47e98', 'Sustainable Running Shoes', '129.99', 400),
('4f7c13', 'Reusable Beeswax Wraps', '19.99', 5),
('9dc6ab', 'Organic Cotton Bath Towel Set', '39.99', 10),
('e32d51', 'Vintage Kicks', '79.99', 500),
('2a65fd', 'Organic Superfood Mix', '29.99', 300),
('ac9b42', 'Eco-Friendly Yoga Mat', '49.99', 100),
('d5b356', 'Recycled Plastic Water Bottle', '19.99', 10),
('a09072', 'Retro Sneakers', '79.99', 500),
('bc10f3', 'Organic Cotton Face Mask', '9.99', 5),
('cb8c01', 'Raw Denim Jeans', '99.99', 250),
('fb9d6e', 'Sustainable Bamboo Sunglasses', '49.99', 30),
('1c4b21', 'Portable Solar Charger', '69.99', 200),
('7e7d8a', 'Reusable Grocery Bag Set', '24.99', 5),
('2a9bcf', 'Minimalist Phone Case', '14.99', 50),
('bba502', 'Handmade Leather Wallet', '39.99', 20),
('c1b97f', 'Bluetooth Earbuds', '69.99', 25),
('8a9d15', 'Smart Thermostat', '129.99', 50),
('44cdeb', 'Bamboo Toothbrush Set', '14.99', 5),
('dc4b18', 'Recycled Glass Water Bottle', '29.99', 10);