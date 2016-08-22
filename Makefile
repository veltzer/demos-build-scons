.PHONY: all
all: tools.stamp

tools.stamp: apt.yaml
	$(info doing [$@])
	@templar_cmd install_deps
	@make_helper touch-mkdir $@

.PHONY: clean
clean:
	@git clean -qffxd
