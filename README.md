# iec61850_mms_scapy

Scapy definitions (partially ASN.1) for a small subset of IEC 61850-8-1 MMS messages.
Basic functionality of intermediary layers (tpkt, cotp, iso8327-1, iso8823, and iso8650-1) has been implemented.

To bind layers, run:

```python
import iec61850_mms
iec61850_mms.bind_layers()
```

### Supported packet types
```plain
MMS:
    -   ConfirmedRequest (read, write, getnamelist)
    -   InitiateRequest
    -   InitiateResponse

ACSE/ISO 8650-1:
    - AARQ
    - AARE

ISO 8823:
    - CP
    - CPA
    - CPC

ISO 8327-1:
    - User Data (DT)
    - Connect (CN)
    - Accept (AC)

COTP:
    - Data (DT)
    - Connection Requests (CR)
    - Connection Responses (CC)
```
