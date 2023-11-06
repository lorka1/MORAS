Require Import Bool.
Notation "!" := negb (at level 0).

Goal forall X Y,
(X && !Y) || (!X && !Y) || (!X && Y) = (!X || !Y).
Proof. intros. destruct X, Y. 
- simpl. reflexivity.
- simpl. reflexivity.
- simpl. reflexivity.
- simpl. reflexivity. Qed.
