from graphviz import Digraph
from collections import defaultdict

class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
    #DFA cizimi
    def visualize(self, filename='dfa'):
        dot = Digraph()
        for state in self.states:
            if state in self.accept_states:
                dot.node(state, state, shape='doublecircle')  
            else:
                dot.node(state, state, shape='circle')  
        dot.node('', '', shape='none')  
        dot.edge('', self.start_state)

        for (src, char), tgt in self.transition_function.items():
            dot.edge(src, tgt, label=char)

        dot.render(filename, format='png', cleanup=True)
        print(f"{filename}.png has been created.")

    def minimize(self):
        """DFA minimizasyon işlemini gerçekleştirir."""
        reverse_tf = defaultdict(set)
        for (src, lbl), tgt in self.transition_function.items():
            reverse_tf[tgt].add((src, lbl))

        non_accept_states = self.states - self.accept_states
        partitions = [frozenset(self.accept_states), frozenset(non_accept_states)]
        work_list = partitions.copy()

        while work_list:
            A = work_list.pop()
            for c in self.alphabet:
                X = frozenset(src for tgt in A for (src, lbl) in reverse_tf[tgt] if lbl == c)
                updates = []
                for Y in partitions:
                    diff = Y - X
                    inter = Y & X
                    if diff and inter:
                        partitions.remove(Y)
                        partitions.extend([frozenset(diff), frozenset(inter)])
                        if Y in work_list:
                            work_list.remove(Y)
                            work_list.extend([frozenset(diff), frozenset(inter)])
                        else:
                            work_list.append(frozenset(diff) if len(diff) < len(inter) else frozenset(inter))

        new_states = {part: f's{index}' for index, part in enumerate(partitions)}
        new_start_state = next((new_states[part] for part in partitions if self.start_state in part), None)
        if new_start_state is None:
            raise ValueError("Başlangıç durumu hiçbir partisyona dahil edilmedi.")

        new_accept_states = {new_states[part] for part in partitions if part & self.accept_states}
        new_tf = {}
        for part in partitions:
            representative = next(iter(part))
            for lbl in self.alphabet:
                if (representative, lbl) in self.transition_function:
                    target = self.transition_function[(representative, lbl)]
                    new_tf[(new_states[part], lbl)] = new_states[next(p for p in partitions if target in p)]

        minimized_dfa = DFA(set(new_states.values()), self.alphabet, new_tf, new_start_state, new_accept_states)
        self.print_grammar(minimized_dfa, new_states)  # yeni durumlari yazdirma
        return minimized_dfa

    @staticmethod
    def print_grammar(dfa, state_mapping):
        print("\nMinimize Edilmiş DFA'nın Grameri:") #minimize edilmiş dfa
        print(f"Başlangıç Durumu: {dfa.start_state}")
        print(f"Kabul Durumları: {', '.join(dfa.accept_states)}")
        print("Geçiş Fonksiyonları:")
        for (src, char), tgt in dfa.transition_function.items():
            print(f"{src} --{char}--> {tgt}")
        print("Yeni Durumlar:")
        for old_states, new_state in state_mapping.items():
            print(f"{new_state}: {', '.join(old_states)}")


def get_input(prompt):
    #Kullanicidan veri almak için 
    return input(prompt)

def main():
    print("DFA Minimization Program")
    print("------------------------")
    states = set(get_input("Durumları giriniz (boşlukla ayırarak): ").split())
    alphabet = set(get_input("Alfabeyi giriniz (boşlukla ayırarak): ").split())
    start_state = get_input("Başlangıç durumunu giriniz: ")
    if start_state not in states:
        raise ValueError(f"Başlangıç durumu '{start_state}' durumlar arasında değil.")
    
    accept_states = set(get_input("Kabul edilen durumları giriniz (boşlukla ayırarak): ").split())
    if not accept_states.issubset(states):
        raise ValueError("Kabul edilen durumlar genel durumlar arasında değil.")

    transition_function = {}
    print("Geçiş fonksiyonunu giriniz (örneğin, 'q0 0 q1'). 'Bitti' yazarak bitirin:")
    while True:
        transition = get_input("Geçiş (bitişik durum ve girdi, 'Bitti' yazarak bitirin): ")
        if transition.lower() == "bitti":
            break
        parts = transition.split()
        if len(parts) != 3:
            print("Hatalı giriş! Lütfen 'q0 0 q1' formatında giriniz.")
            continue
        src_state, input_char, dest_state = parts
        if src_state not in states or dest_state not in states or input_char not in alphabet:
            print("Geçiş hatalı! Lütfen tanımlı durumlar ve alfabeye göre geçiş giriniz.")
            continue
        transition_function[(src_state, input_char)] = dest_state

    dfa = DFA(states, alphabet, transition_function, start_state, accept_states)
    print("Orijinal DFA görselleştiriliyor...")
    dfa.visualize('original_dfa')

    print("DFA minimize ediliyor...")
    minimized_dfa = dfa.minimize()
    print("Minimize edilmiş DFA görselleştiriliyor...")
    minimized_dfa.visualize('minimized_dfa')

if __name__ == "__main__":
    main()
