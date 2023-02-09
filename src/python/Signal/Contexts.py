from Contexts.Functor import ListFunctor
from Contexts.Applicative import ListApplicative, liftA2
from Contexts.Monad import ListMonad

from Signal.Types import sig_0, sig_1, sig_3

Sigor=ListFunctor[sig_0|sig_1|sig_3]
Sigive=ListApplicative[sig_0|sig_1|sig_3]
SigMonad=ListMonad[sig_0|sig_1|sig_3]
SigLiftA2=liftA2
