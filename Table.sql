CREATE TABLE company_info (
    Symbol TEXT PRIMARY KEY,
    Company_Name TEXT NOT NULL,
    Industry TEXT,
    Market_Cap TEXT  -- Stored as text for values like '45.3B'; can be parsed in code
);


CREATE TABLE stock_market_data (
    Date DATE NOT NULL,
    Open NUMERIC,
    High NUMERIC,
    Low NUMERIC,
    Close NUMERIC,
    Adj_Close NUMERIC,
    Volume BIGINT,
    Name TEXT,  -- Ticker symbol, used to join with company_info.Symbol
    Company_Name TEXT,
    PRIMARY KEY (Date, Name)
);