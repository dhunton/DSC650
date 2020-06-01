# Data Sets

---

## Berkley DeepDrive

Data from [Berkley DeepDrive][berkley-deepdrive] is found in `data/external/bdd`.

### License

Copyright ©2018. The Regents of the University of California (Regents). All Rights Reserved. 

Permission to use, copy, modify, and distribute this software and its documentation for educational, research, and not-for-profit purposes, without fee and without a signed licensing agreement; and permission use, copy, modify and distribute this software for commercial purposes (such rights not subject to transfer) to BDD member and its affiliates, is hereby granted, provided that the above copyright notice, this paragraph and the following two paragraphs appear in all copies, modifications, and distributions. Contact The Office of Technology Licensing, UC Berkeley, 2150 Shattuck Avenue, Suite 510, Berkeley, CA 94720-1620, (510) 643-7201, otl@berkeley.edu, http://ipira.berkeley.edu/industry-info for commercial licensing opportunities.

IN NO EVENT SHALL REGENTS BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF REGENTS HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

REGENTS SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, PROVIDED HEREUNDER IS PROVIDED "AS IS". REGENTS HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

## Enron Emails

The folder `data/external/enron` contains a partial copy of the [Enron Email dataset][enron-dataset].


## Large Movie Review

[Large Movie Review Dataset][large-movie-review] contains 25,000 movie reviews from IMDB and can be found in `data/external/imdb`.

## OpenFlights

### License 

The OpenFlights Airport, Airline, Plane and Route Databases are made available under the [Open Database License][opendb-license]. Any rights in individual contents of the database are licensed under the [Database Contents License][db-contents-license]. In short, these mean that you are welcome to use the data as you wish, if and only if you both acknowledge the source and and license any derived works made available to the public with a free license as well.

See [OpenFlights Data][openflights-data] for more detailed documentation. 

### Data 

OpenFlights data is found in `data/external/openflights`.  Data copied from the [OpenFlights Github Repo][openflights-github].

!!! note
    The special value **\\N** is used for \"NULL\" to indicate that no value is available

#### Airports

| Field          | Type          | Nullable? | Notes                |
|----------------|---------------|-----------|----------------------|
| airport_id     | int           | No        | Primary Key          |
| name           | text          | Yes       |                      |
| city           | text          | Yes       |                      |
| country        | text          | Yes       |                      |
| iata           | varchar(3)    | Yes       |                      |
| icao           | varchar(4)    | Yes       |                      |
| latitude       | double        | No        |                      |
| longitude      | double        | No        |                      |
| altitude       | int           | Yes       |                      |
| timezone       | float         | Yes       |                      |
| dst            | char(1)       | Yes       |                      |
| tz_id          | text          | Yes       |                      |
| type           | text          | Yes       |                      |
| source         | text          | Yes       |                      |

#### Airlines

| Field          | Type          | Nullable? | Notes                |
|----------------|---------------|-----------|----------------------|
| airline_id     | int           | No        | Primary Key          |
| name           | text          | No        |                      |
| alias          | text          | Yes       |                      |
| iata           | varchar(2)    | Yes       |                      |
| icao           | varchar(3)    | Yes       |                      |
| callsign       | text          | Yes       |                      |
| country        | text          | Yes       |                      |
| active         | boolean       | No        | Default value FALSE  | 

#### Routes

| Field          | Type          | Nullable? | Notes                |
|----------------|---------------|-----------|----------------------|
| airline        | varchar(3)    | Yes       |                      |
| airline_id     | int           | Yes       |                      |
| src_airport    | varchar(4)    | Yes       |                      |
| src_airport_id | int           | Yes       |                      |
| dst_airport    | varchar(4)    | Yes       |                      |
| dst_airport_id | int           | Yes       |                      |
| codeshare      | boolean       | Yes       | Default value FALSE  |
| stops          | int           | Yes       |                      | 
| equipment      | text          | Yes       |                      | 

`airline_id`, `src_airport_id`, and `dst_airport_id` form a unique key

#### Planes

| Field          | Type          | Nullable? | Notes                |
|----------------|---------------|-----------|----------------------|
| name           | text          | Yes       |                      |
| iata           | varchar(3)    | Yes       |                      |
| icao           | varchar(4)    | Yes       |                      |

#### Countries

| Field          | Type          | Nullable? | Notes                |
|----------------|---------------|-----------|----------------------|
| name           | text          | Yes       |                      |
| iso_code       | varchar(2)    | Yes       |                      |
| dafif_code     | varchar(2)    | Yes       |                      |

!!! note 
    Some entries have DAFIF codes, but not ISO codes. These are
    primarily uninhabited islands without airports, and can be ignored
    for most purposes.
    
## Tidynomicon

Data copied from the [Tidynomicon Github repository][tidynomicon-github]. 

### License

*This is a human-readable summary of (and not a substitute for) the license.
Please see <https://creativecommons.org/licenses/by/4.0/legalcode> for the full legal text.*

This work is licensed under the Creative Commons Attribution 4.0
International license (CC-BY-4.0).

**You are free to:**

- **Share**---copy and redistribute the material in any medium or
  format

- **Remix**---remix, transform, and build upon the material for any
  purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the
license terms.

**Under the following terms:**

- **Attribution**---You must give appropriate credit, provide a link
  to the license, and indicate if changes were made. You may do so in
  any reasonable manner, but not in any way that suggests the licensor
  endorses you or your use.

- **No additional restrictions**---You may not apply legal terms or
  technological measures that legally restrict others from doing
  anything the license permits.

**Notices:**

You do not have to comply with the license for elements of the
material in the public domain or where your use is permitted by an
applicable exception or limitation.

No warranties are given. The license may not give you all of the
permissions necessary for your intended use. For example, other rights
such as publicity, privacy, or moral rights may limit how you use the
material.


[berkley-deepdrive]: https://bdd-data.berkeley.edu/
[cc-licenses]: https://creativecommons.org/licenses/by/4.0/legalcode
[db-contents-license]: https://opendatacommons.org/licenses/dbcl/1.0/
[enron-dataset]: https://www.cs.cmu.edu/~enron/
[large-movie-review]: https://ai.stanford.edu/~amaas/data/sentiment/
[opendb-license]: https://opendatacommons.org/licenses/odbl/1.0/
[openflights-data]: https://openflights.org/data.html
[openflights-github]: https://github.com/jpatokal/openflights
[tidynomicon]: http://tidynomicon.tech/
[tidynomicon-github]: https://github.com/gvwilson/tidynomicon

