try:
    import neovim

    @neovim.plugin
    class Entrypoint:
        def __init__(self, nvim):
            self.nvim = nvim
            self.registry = Registry(nvim)

        @neovim.function('_demo_regget', sync=True)
        def regget(self, args):
            return self.registry.get(*args)

        @neovim.function('_demo_regset', sync=True)
        def regset(self, args):
            self.registry.set(*args)

except ImportError:
    pass


class Registry:
    def __init__(self, nvim):
        self.nvim = nvim

    def get(self, regname):
        return self.nvim.call('getreg', regname)

    def set(self, regname, value):
        self.nvim.call('setreg', regname, value)
