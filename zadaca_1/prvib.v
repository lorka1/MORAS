Require Import Bool.
Notation "!" := negb (at level 0).

Goal forall X Y Z, 
!(!X && Y && Z) && !(X && Y && !Z) && (X && !Y && Z) = (X && !Y && Z).
Proof. intros. destruct X, Y, Z.
- simpl. reflexivity.
- simpl. reflexivity.
- simpl. reflexivity.
- simpl. reflexivity.
- simpl. reflexivity.
- simpl. reflexivity.
- simpl. reflexivity.
- simpl. reflexivity.
Qed.