### SQLite RDBMS

___

* Relational database management system
* Use in Python with the `sqlite3` module
* SQLite is light in terms of setup, administration and resources

#### No Server Needed

* SQLite is serverless
* SQLite database are local with files stored on disk
* Accessing and manipulating data is extremely quick
* No Installation needed
* No server configurations needed

#### Self-Contained

* SQLite does not require many external libraries
* SQLite can run on many different platforms and environments

#### ACID-Compliant

* All transactions in SQLite are ACID-compliant
* A transaction is a set of queries you want to take place at once
* Atomic, consistent, isolated and durable (ACID)
* Your database will never be in a halp-completed state

#### SQLite

* Great database for prototyping
* Ability to port to a larger database later on

### Object-Relational Mapping (ORM)

___

* Sometimes queries can seem out of place
* ORMs help you work with databases in a more Pythonic way
* Various libraries implement ORM-like functionality
* `SQLAlchemy` is one of the most popular ORMs for relational databases in Python
* `SQLAlchemy` works with varying web frameworks and `SQLite`, `MySQL` and `Postgres`

#### SQLAlchemy

* `SQLAlchemy` is a large SQL toolkit with lots of different components
* The two largest components are `SQLAlchemy Core` and `SQLAlchemy ORM`
* `SQLAlchemy Core` has a schema-centric view while `SQLAlchemy ORM` uses an object-centric view

#### Pros and Cons of ORMs

* **Pros**
    * Abstract database layer
    * Speed up development
    * Easier to prototype with
    * Fast queries out of the box
* **Cons**
    * Shifts database complexity into the application code rather than keeping it separate
    * Can prevent you from understanding what SQL is doing under the hood

#### SQLAlchemy 2.0

* Core and ORM are becoming more integrated
* `SQLAlchemy` 2.0 is still in beta and being finalized
