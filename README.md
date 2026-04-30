# knowb4-parser

This is a python script (app) that decodes an hidden knowb4 url and reveals the real one:

**From**

    $> python3 . --url "https://links.eu1.defend.egress.com/Warning?crId=69f33d43df0b11aff2252726&Domain=tiuim.com&Threat=eNpzrShJLcpLzAEADmkDRA%3D%3D&Lang=en&Base64Url=eNrLKCkpKLbS10_PLMkoTdJLzs_VTywtycjPS9XPzssvTzLRTUlNzk9J1S2oBABhwhAK&@OriginalLink=github.com" https://links.eu1.defend.egress.com/Warning?crId=12fffd43340b11ade2236718&Domain=mydomain.com&Threat=RDMRAss%3D%3D&Lang=en&Base64Url=eNrLKCkpKLbS10_PLMkoTdJLzs_VTywtycjPS9XPzssvTzLRTUlNzk9J1S2oBABhwhAK&@OriginalLink=github.com

**To**

    https://github.com/authone/knowb4-decode-py

**Using**
You need python3 > 3.11 to run it

    $> python3 . --help
        -h                      print this help and exit.
        -v, --version           print application version and exit.
        -t, --text              simple text output
        -u, --url url           knowb4 egress URL to parse
