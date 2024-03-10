# Postmortem

## Issue Summary

- **Duration of the outage:** The outage occurred from 3:00 PM to 4:30 PM (GMT-5) on August 15th, 2023.
- **Impact:** The user authentication service was down for the duration of the outage, resulting in users being unable to log in to their accounts. Approximately 25% of all users were affected, leading to a significant drop in user activity and potential revenue loss.
- **Root Cause:** The outage was caused by a database query optimization that inadvertently led to a deadlock condition, halting the authentication service.

## Timeline

- 3:00 PM (GMT-5) **Issue Detection:** The issue was detected at 3:00 PM through a monitoring alert indicating a spike in failed authentication attempts.
- 3:15 PM (GMT-5) **Actions Taken:** I immediately investigated the database logs, initially suspecting a potential DDoS attack due to the sudden surge in failed login attempts. However, this assumption was later discarded after further analysis revealed the deadlock in the database queries.
- 3:45 PM (GMT-5) **Misleading Paths:** The initial investigation focused on the network infrastructure and potential security breaches before shifting to database performance analysis.
- 4:30 PM (GMT-5) **Resolution:** The deadlock condition was resolved by tweaking the database query optimization and implementing a more robust deadlock detection and resolution mechanism.

## Root Cause and Resolution

- The issue stemmed from an unintended database query optimization that created a deadlock condition, blocking user authentication requests.
- The issue was fixed by reverting the database query optimization to its previous configuration and implementing a deadlock detection and resolution mechanism within the database management system.

## Corrective and Preventative Measures

- **Improvements:** Implement comprehensive testing protocols for database optimizations and potential deadlock scenarios. Enhance monitoring and alerting systems to promptly detect and respond to similar incidents in the future.
- **Tasks:**
  - Conduct a thorough review of all recent database optimizations to identify potential performance pitfalls.
  - Enhance documentation and communication protocols for critical system changes to prevent unintended consequences.
  - Implement additional monitoring specifically targeting authentication service performance and database deadlock scenarios.
  - Conduct a post-incident review meeting to analyze the response and identify further areas for improvement.

In conclusion, the outage stemmed from an unintended consequence of a database query optimization, resulting in a significant impact on user access. The rapid response and resolution prevented further prolonged downtime, and the incident serves as a catalyst for implementing robust preventive measures to safeguard against similar issues in the future.
