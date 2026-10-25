import unittest
from astrea_oracle import AstreaOracle, Profile, LocalNarrator

class TestCore(unittest.TestCase):
    def setUp(self):
        self.alice = Profile("alice", 26, True, ("music", "hiking"), ("kindness", "curiosity"), "aries")
        self.bob = Profile("bob", 28, True, ("hiking", "chess"), ("kindness", "humor"), "libra")
        self.engine = AstreaOracle()

    def test_match_is_explainable(self):
        result = self.engine.match(self.alice, self.bob)
        self.assertEqual(result.shared_values, ("kindness",))
        self.assertEqual(result.shared_interests, ("hiking",))
        self.assertAlmostEqual(result.overlap_score, 33.33)
        self.assertIn("No astrology", result.explanation)
        self.assertIn("Symbolic", result.symbolic_note)

    def test_zodiac_not_used_in_score(self):
        other = Profile("alice", 26, True, self.alice.interests, self.alice.values, "scorpio")
        self.assertEqual(self.engine.match(self.alice, self.bob).overlap_score,
                         self.engine.match(other, self.bob).overlap_score)

    def test_refuse_no_consent(self):
        other = Profile("other", 30, False)
        with self.assertRaises(PermissionError):
            self.engine.match(self.alice, other)

    def test_refuse_minor(self):
        other = Profile("teen", 17, True)
        with self.assertRaises(PermissionError):
            self.engine.match(self.alice, other)

    def test_refuse_consequential_purpose(self):
        with self.assertRaises(ValueError):
            self.engine.match(self.alice, self.bob, purpose="employment")

    def test_refuse_same_profile(self):
        with self.assertRaises(ValueError):
            self.engine.match(self.alice, self.alice)

    def test_invalid_sign(self):
        with self.assertRaises(ValueError):
            Profile("wrong", 24, True, zodiac_sign="sun")

    def test_score_zero_when_no_tags(self):
        a, b = Profile("a", 20, True), Profile("b", 20, True)
        self.assertEqual(self.engine.match(a, b).overlap_score, 0.0)

    def test_narrator_is_not_prediction(self):
        text = LocalNarrator().narrate("Shared interests include hiking.")
        self.assertIn("not a prediction", text)

if __name__ == "__main__":
    unittest.main()
