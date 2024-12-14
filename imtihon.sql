CREATE TABLE IF NOT EXISTS manufacturer(
	manufacturer_id SERIAL PRIMARY KEY,
	manufacturer_name VARCHAR(183)NOT NULL);

CREATE TABLE IF NOT EXISTS products(
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(95) NOT NULL,
	product_price VARCHAR NOT NULL,
	STOCK INTEGER,
	manufacturer_id INTEGER REFERENCES manufacturer(manufacturer_id));
	
	
INSERT INTO manufactureR(manufacturer_name) VALUES
('mercurial'),
('totto');
SELECT * FROM manufacturer;


INSERT INTO products (product_id, product_name, product_price, stock) VALUES
(1, 'butsa', 10, 4),
(2, 'keta', 6, 6),

select product_name, product_price > avg(product_price) from product;

update products set product_price = 1210 where product_id = 1

update products set product_price = product_price + 20;

delete product where product_id = 1,
delete products

alter table manufacturer
add column manufacturer_year data default current_date;

alter table manufactures


drop table manufacturer;
drop table product;