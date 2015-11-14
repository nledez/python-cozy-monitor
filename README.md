Installation
============

```
[ ! -d virtualenv ] && virtualenv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
```

Developpment installation
============

```
[ ! -d virtualenv ] && virtualenv virtualenv
source virtualenv/bin/activate
pip install -r requirements-tests.txt
```

Launch tests:
In "TDD" mode:
```
sniffer -x--with-xunit -x--with-coverage -x--cover-tests -x--cover-html -x--cover-xml -x--cover-tests -x--cover-package=cozy_monitor,tests tests/
```

In one shoot mode:
```
nosetests --with-xunit --with-coverage --cover-tests --cover-html --cover-xml --cover-tests --cover-package=cozy_monitor,tests tests/
```
