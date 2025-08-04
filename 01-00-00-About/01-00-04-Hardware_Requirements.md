# Hardware Requirements

- The following hardware requirements assume the default check intervals of 5 minutes.

-   If extensive logging is required in the environment, it is advisable to utilize 2 server, clustered environment. 


|Hosts|CPU cores|RAM|Storage|
|:----|:--------|:--|:------|
|Up to 300|8    |16 GB|500 GB SSD|
|Up to 1000|12  |24 GB|500 GB SSD|
|Over 2000|12   |32 GB|1 TB SSD|

|Partition Set Up (Up to 1000 hosts)||
|:------|:-------|
|/| 10 GB|
|/opt| 100 GB|
|/tmp| 3 GB|
|/home| 10 GB|
|/data| 60 GB|
|/var| 20 GB|
|/var/lib| 120 GB|
|/var/log| 35 GB|
|/var/log/audit| 6 GB|

|Partition Set Up (Over 2000 hosts)||
|:------|:-------|
|/| 20 GB|
|/opt| 100 GB|
|/tmp| 3 GB|
|/home| 10 GB|
|/data| 60 GB|
|/var| 20 GB|
|/var/lib| 500 GB|
|/var/log| 35 GB|
|/var/log/audit| 6 GB|

<blockquote style="border-left: 8px solid orange; padding: 15px;"> <b>Note</b>: 
For installations above 2000 hosts we recommend involving EMCA engineers for the topology design.
</blockquote>
