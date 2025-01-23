all: check tests

.PHONY: \
		all \
		clean \
		check \
		tests

clean:
	rm --force --recursive .*_cache
	rm --force --recursive src/__pycache__
	rm --force --recursive tests/__pycache__

check:
	black --check --line-length 100 src

tests:
	pytest --verbose