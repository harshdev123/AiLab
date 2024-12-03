class KnowledgeBase:
    def __init__(self):
        self.facts = set()  # Set to store known facts
        self.rules = []  # List to store inference rules

    def add_fact(self, fact):
        """Add a single fact to the knowledge base."""
        self.facts.add(fact)

    def add_rule(self, rule):
        """Add a rule (function) to the knowledge base."""
        self.rules.append(rule)

    def forward_reason(self):
        """Perform forward reasoning to derive new facts."""
        new_facts = set()
        while True:
            for rule in self.rules:
                inferred = rule(self.facts)
                # Add only new facts that aren't already in the knowledge base
                new_facts.update(inferred - self.facts)
            if not new_facts:
                break
            self.facts.update(new_facts)
            new_facts.clear()

    def query(self, fact):
        """Check if a fact exists in the knowledge base."""
        return fact in self.facts


# Define rules
def rule_american_criminal(facts):
    """If an American sells weapons to hostile nations, they are a criminal."""
    inferred = set()
    for fact in facts:
        if fact.startswith("Sells("):  # Find sells facts
            parts = fact[6:-1].split(", ")  # Extract parts: Sells(person, weapon, country)
            person, weapon, country = parts[0], parts[1], parts[2]
            if f"American({person})" in facts and f"Weapon({weapon})" in facts and f"Hostile({country})" in facts:
                inferred.add(f"Criminal({person})")
    return inferred


def rule_hostile_enemy(facts):
    """Enemies of America are hostile."""
    inferred = set()
    for fact in facts:
        if fact.startswith("Enemy("):
            parts = fact[6:-1].split(", ")  # Extract parts: Enemy(country, America)
            country = parts[0]
            inferred.add(f"Hostile({country})")
    return inferred


def rule_weapons_from_missiles(facts):
    """Missiles are weapons."""
    inferred = set()
    for fact in facts:
        if fact.startswith("Missile("):
            missile = fact[8:-1]  # Extract missile name
            inferred.add(f"Weapon({missile})")
    return inferred


def rule_sells_missiles(facts):
    """If Country A owns missiles, Robert sold them."""
    inferred = set()
    for fact in facts:
        if fact.startswith("Owns("):
            parts = fact[5:-1].split(", ")  # Extract parts: Owns(country, item)
            country, item = parts[0], parts[1]
            if f"Missile({item})" in facts:
                inferred.add(f"Sells(Robert, {item}, {country})")
    return inferred


# Initialize the knowledge base
kb = KnowledgeBase()

# Add facts
kb.add_fact("American(Robert)")
kb.add_fact("Enemy(A, America)")
kb.add_fact("Owns(A, T1)")
kb.add_fact("Missile(T1)")

# Add rules
kb.add_rule(rule_american_criminal)
kb.add_rule(rule_hostile_enemy)
kb.add_rule(rule_weapons_from_missiles)
kb.add_rule(rule_sells_missiles)

# Perform forward reasoning
kb.forward_reason()

# Query the knowledge base
query = "Criminal(Robert)"
print(f"Is '{query}' true? {'Yes' if kb.query(query) else 'No'}")
