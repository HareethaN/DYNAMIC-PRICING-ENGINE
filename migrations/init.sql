CREATE TABLE products (
  product_id BIGINT PRIMARY KEY,
  sku TEXT,
  name TEXT,
  category TEXT,
  base_cost_cents INTEGER,
  current_price_cents INTEGER,
  min_price_cents INTEGER,
  max_price_cents INTEGER,
  inventory_qty INTEGER,
  last_updated TIMESTAMP DEFAULT NOW()
);

CREATE TABLE price_history (
  id SERIAL PRIMARY KEY,
  product_id BIGINT REFERENCES products(product_id),
  old_price_cents INTEGER,
  new_price_cents INTEGER,
  reason TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  product_id BIGINT,
  user_id BIGINT NULL,
  event_type TEXT,
  price_cents INTEGER,
  timestamp TIMESTAMP,
  metadata JSONB
);
