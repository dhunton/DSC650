# Latency

*Latency Numbers Every Data Scientist Should Know*

In the 2000s, Jeff Dean, a Google Senior Fellow in their Research Group, [presented a list of latency numbers that every programmer should know](http://highscalability.com/numbers-everyone-should-know). These numbers describe how long it takes to perform certain actions within distributed programs. Since then, it has been [updated](http://highscalability.com/blog/2013/1/15/more-numbers-every-awesome-programmer-must-know.html) and [expanded upon](https://medium.com/@hondanhon/more-latency-numbers-every-programmer-should-know-3142f0cf614d).

Below is yet another update on these numbers with data taken from [Colin Scott](https://github.com/colin-scott/interactive_latencies), a Berkeley researcher. An interactive version of this repository can be found [here](https://colin-scott.github.io/personal_website/research/interactive_latency.html).

---

| Action                             | Latency (ns)[^1]| Latency (&mu;)[^2]| Latency (ms)[^3]|
|------------------------------------|----------------:|------------------:|----------------:|
| L1 cache reference                 |            1 ns |                   |                 |
| Branch mispredict                  |            3 ns |                   |                 |
| L2 cache reference                 |            4 ns |                   |                 |
| Mutex lock/unlock                  |           17 ns |                   |                 |
| Main memory reference              |          100 ns |                   |                 |
| Compress 1KB with Zippy            |        2,000 ns |         2 &mu;s   |                 |
| Send 1KB over 1 Gbps network       |       10,000 ns |        10 &mu;s   |                 |
| SSD random read                    |       16,000 ns |        16 &mu;s   |                 |
| Read 1 MB sequentially from SSD    |       49,000 ns |        49 &mu;s   |                 |
| Read 1 MB sequentially from memory |      250,000 ns |       250 &mu;s   |                 |
| Round trip within same datacenter  |      500,000 ns |       500 &mu;s   |                 |
| Read 1 MB sequentially from disk   |      825,000 ns |       825 &mu;s   |                 |
| Disk seek                          |    2,000,000 ns |     2,000 &mu;s   |   2 ms          |
| Send packet CA->Netherlands->CA    |  150,000,000 ns |   150,000 &mu;s   | 150 ms          |


*Notes*

[^1]: 1 ns = 10<sup>-9</sup> seconds
[^2]: 1 &mu;s = 10<sup>-6</sup> seconds = 1,000 ns
[^3]: 1 ms = 10<sup>-3</sup> seconds = 1,000 &mu;s = 1,000,000 ns

[jeff-dean]: https://research.google/people/jeff/
