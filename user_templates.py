class myTemplates(object):
    name = "myTemplate"
    style = 'camelCase' # can also be snakeCase
    getter = """
    public function get%(normalizedName)s() {
        return $this->%(name)s;
    }
"""

    setter = """
    public function set%(normalizedName)s(%(typeHint)s $%(name)s) {
        $this->%(name)s = $%(name)s;
    }
"""
