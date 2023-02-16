from Contexts.Functor import ListFunctor
from Contexts.Applicative import ListApplicative, liftA2
from Contexts.Monad import ListMonad
from Contexts.Foldable import ListFoldable

from Signal.Types import signum, sig_0

Sigor=ListFunctor[signum|sig_0|tuple[sig_0,sig_0,sig_0]]
Sigive=ListApplicative[signum|sig_0|tuple[sig_0,sig_0,sig_0]]
SigMonad=ListMonad[signum|sig_0|tuple[sig_0,sig_0,sig_0]]
SigLiftA2=liftA2
SigFoldable=ListFoldable[signum|sig_0|tuple[sig_0,sig_0,sig_0]]
