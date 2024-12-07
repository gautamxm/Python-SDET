# Calculate the difference in days between two dates: 15th August 2025 and 1st January 2025

import datetime

date1 = datetime.date(2025, 8, 15)
date2 = datetime.date(2025, 1, 1)
diff = date2 - date1
print(abs(diff).days)    # 226