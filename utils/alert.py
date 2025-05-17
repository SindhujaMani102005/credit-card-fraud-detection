
def send_alert(transaction):
    print("\n⚠️ FRAUD ALERT")
    print(f"Amount: {transaction.get('Amount', 'N/A')}, Time: {transaction.get('Time', 'N/A')}")
    print("Action: Transaction flagged and logged.")
