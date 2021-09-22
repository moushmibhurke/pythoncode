class TestClass:
    def test_one(self):
        x="eureka"
        assert 'r' in x

    def test_two(self):
        x="hello"
        assert hasattr(x,"check")

#grouping all test in one class