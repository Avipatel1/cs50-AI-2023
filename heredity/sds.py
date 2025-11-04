family = {'Lily', 'Harry', 'James'}
family2 = {'Arthur', 'Charlie', 'Fred', 'Ginny', 'Molly', 'Ron'}

one_gene = {"Harry"} 
two_genes = {"James"} 
trait = {"Harry", "James"}

zero_genes = set()
for member in family:
    if member not in one_gene and member not in two_genes:
        zero_genes.add(member)
print(zero_genes)

no_trait = family.difference(trait)
print(no_trait)