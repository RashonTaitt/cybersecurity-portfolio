# Incident Report 001: Suspicious SSH Authentication

## 1. Incident Summary

**Incident ID:** INC-001  
**Incident Type:** Suspected Brute-Force Authentication  
**Severity:** High (Preliminary Assessment)  
**Status:** Open - Further Investigation Required  
**Environment:** Simulated Linux SSH server  
**Date of Activity:** October 31, 2026

## 2. Executive Summary

Analysis of simulated SSH authentication logs identified repeated failed login attempts from two source IP addresses. The most concerning activity originated from `185.220.101.45`, which generated five failed login attempts against multiple accounts before successfully authenticating to the `backup` account.

This sequence is suspicious and requires further investigation. The available evidence does not independently confirm that the account was compromised.

## 3. Evidence and Findings

### Finding 1: Repeated Authentication Failures

- **Source IP:** `185.220.101.45`
- **Failed attempts:** 5
- **Targeted accounts:** `admin`, `root`
- **Time range:** 08:15:02 to 08:15:26

### Finding 2: Successful Authentication After Failures

- **Source IP:** `185.220.101.45`
- **Account:** `backup`
- **Time:** 08:18:01
- **Assessment:** Suspicious authentication following repeated failures from the same source.

### Finding 3: Additional Failed Authentication Activity

- **Source IP:** `45.33.32.156`
- **Failed attempts:** 3
- **Targeted accounts:** `test`, `root`
- **Time range:** 08:17:11 to 08:19:45

### Finding 4: Other Successful Authentication

- **Source IP:** `192.168.1.15`
- **Account:** `rashon`
- **Time:** 08:16:02
- **Assessment:** Successful authentication observed. Authorization and expected activity have not been independently verified.

## 4. Investigation Assessment

The repeated failures against multiple accounts, followed by a successful login from the same source IP, are consistent with suspicious authentication activity that may involve brute-force attempts.

The current evidence is insufficient to establish whether the `backup` login was authorized or whether unauthorized access occurred.

## 5. Recommended Next Steps

1. Verify whether the `backup` login was expected and authorized.
2. Review additional authentication and system logs around the event.
3. Investigate activity performed by the `backup` account after login.
4. Check for unexpected file changes, new accounts, or configuration changes.
5. Preserve relevant logs and document the investigation timeline.
6. Follow the organization's incident response procedures if unauthorized access is confirmed or strongly suspected.

## 6. Limitations

This investigation uses simulated authentication logs created for a cybersecurity learning exercise. No live system was investigated, and no real-world attribution or IP reputation assessment was performed.

## 7. Final Disposition

**Preliminary conclusion:** Suspicious SSH authentication requiring further investigation.

**Confirmed compromise:** Not established by the available evidence.

**Report status:** Preliminary.
