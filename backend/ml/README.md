# ANN: Logic Machine Learning Examples

Very simple examples I've extended from some Coursera/classwork I did.

These should cover the basic **Truth-Tables** for **Classical / Boolean Algebra**. Again, we're striving to *teach* a computer logic here rather than using deductive or Boolean clauses within a programming language to enforce certain kinds of basic inferences (of course we're still using such a programming language under the hood LOL).

> Some humans take a long time to pick up **Classical Logic** (and indeed some never do). Interestingly, our **Deep Learning** network will pick up 100% accurate deduction concepts in a few milliseconds. Be forewarned however that the models are fairly sensitive to the **Learning Rate**. Some will fail to generate a solution if the **Learning Rate** is above `2`, etc. 

1. Implication: set `learning_rate = .25` - added several additional data points for problematic entries (`1&0`):

      ```bash
      python3 ml-implication.py

      Data entry 1&0 with label 0
      Data entry 1&0 with label 0
      Data entry 0&0 with label 1
      Data entry 1&1 with label 1
      Data entry 0&1 with label 1
      [[0.63767246 0.63767246 0.5        0.59235286 0.5       ]]
      Predict: [[ True  True False  True False]]
      [[0.61311754 0.61311754 0.50858915 0.58369335 0.50165377]]
      Predict: [[ True  True  True  True  True]]
      [[0.58494297 0.58494297 0.51256654 0.57073163 0.50390156]]
      Predict: [[ True  True  True  True  True]]
      [[0.55854401 0.55854401 0.51650034 0.55835765 0.50693762]]
      Predict: [[ True  True  True  True  True]]
      [[0.53455388 0.53455388 0.52054879 0.54692571 0.51070039]]
      Predict: [[ True  True  True  True  True]]
      [[0.51327125 0.51327125 0.52481079 0.53660704 0.51510639]]
      Predict: [[ True  True  True  True  True]]
      [[0.49474159 0.49474159 0.52933471 0.52743709 0.52006188]]
      Predict: [[False False  True  True  True]]
      ANN arrived at conclusion: [[False False  True  True  True]] after 6 iterations
      Test set 1: [[ True  True False  True]] from [[1 1]
       [0 0]
       [1 0]
       [0 1]]
      Test set 2: [[ True  True  True  True]] from [[0 1]
       [1 1]
       [1 1]
       [0 1]]
      Test set 3: [[ True  True False False]] from [[1 1]
       [0 1]
       [1 0]
       [1 0]]
      Test set 4: [[ True False  True  True]] from [[0 1]
       [1 0]
       [1 1]
       [0 0]]
      Test set 5: [[ True  True  True False]] from [[0 0]
       [1 1]
       [0 1]
       [1 0]]
      Test set 6: [[False False False False]] from [[1 0]
       [1 0]
       [1 0]
       [1 0]]
      ```

2. Conjunction: set `learning_rate = 1.75`. 

      ```bash
      python3 ml-conjunction.py


      Data entry 0&0 with label 0
      Data entry 1&1 with label 1
      Data entry 0&1 with label 0
      Data entry 1&0 with label 0
      [[0.5        0.35383809 0.5        0.34518138]]
      Predict: [[False False False False]]
      [[0.4076631  0.18692021 0.42413511 0.24969517]]
      Predict: [[False False False False]]
      [[0.39554675 0.14629601 0.33909012 0.28014137]]
      Predict: [[False False False False]]
      [[0.40352847 0.23301112 0.34435528 0.39654987]]
      Predict: [[False False False False]]
      [[0.34540468 0.33021215 0.33890716 0.39069289]]
      Predict: [[False False False False]]
      [[0.27081139 0.43340994 0.3254131  0.33055706]]
      Predict: [[False False False False]]
      [[0.22596828 0.51468278 0.31328059 0.29299712]]
      Predict: [[False  True False False]]
      ANN arrived at conclusion: [[False  True False False]] after 6 iterations
      Test set 1: [[ True False False False]] from [[1 1]
       [0 0]
       [1 0]
       [0 1]]
      Test set 2: [[False  True  True False]] from [[0 1]
       [1 1]
       [1 1]
       [0 1]]
      Test set 3: [[ True  True  True  True]] from [[1 1]
       [1 1]
       [1 1]
       [1 1]]
      Test set 4: [[False False False False]] from [[0 1]
       [0 1]
       [0 1]
       [0 1]]
      ```

3. Disjunction: set `learning_rate = 1.15` - added several additional data points for problematic entries (`0&0`).

      ```bash
      python3 ml-disjunction.py

      Data entry 1&0 with label 1
      Data entry 1&1 with label 1
      Data entry 0&1 with label 1
      Data entry 0&0 with label 0
      Data entry 0&0 with label 0
      Data entry 0&0 with label 0
      [[0.30824369 0.39890757 0.5        0.5        0.5        0.5       ]]
      Predict: [[False False False False False False]]
      [[0.47241598 0.4839943  0.51402865 0.50638105 0.50638105 0.50638105]]
      Predict: [[False False  True  True  True  True]]
      [[0.62499721 0.5724748  0.51452744 0.5175703  0.5175703  0.5175703 ]]
      Predict: [[ True  True  True  True  True  True]]
      [[0.71382256 0.62290442 0.50184748 0.51494063 0.51494063 0.51494063]]
      Predict: [[ True  True  True  True  True  True]]
      [[0.76575736 0.65039114 0.48348243 0.51332844 0.51332844 0.51332844]]
      Predict: [[ True  True False  True  True  True]]
      [[0.79724492 0.66392148 0.46248212 0.51705606 0.51705606 0.51705606]]
      Predict: [[ True  True False  True  True  True]]
      [[0.81416321 0.66644166 0.43995106 0.52492411 0.52492411 0.52492411]]
      Predict: [[ True  True False  True  True  True]]
      [[0.81801644 0.65783083 0.41670887 0.53262744 0.53262744 0.53262744]]
      Predict: [[ True  True False  True  True  True]]
      [[0.80814671 0.63685227 0.39405487 0.53462274 0.53462274 0.53462274]]
      Predict: [[ True  True False  True  True  True]]
      [[0.78644643 0.60391397 0.3792132  0.52714159 0.52714159 0.52714159]]
      Predict: [[ True  True False  True  True  True]]
      [[0.75460192 0.55459573 0.35836505 0.50693162 0.50693162 0.50693162]]
      Predict: [[ True  True False  True  True  True]]
      [[0.72638251 0.52004643 0.35416073 0.49201128 0.49201128 0.49201128]]
      Predict: [[ True  True False False False False]]
      [[0.69175301 0.47281605 0.34677275 0.46875331 0.46875331 0.46875331]]
      Predict: [[ True False False False False False]]
      [[0.67281721 0.45409719 0.35035881 0.46165866 0.46165866 0.46165866]]
      Predict: [[ True False False False False False]]
      [[0.64989287 0.43714271 0.35639164 0.45342592 0.45342592 0.45342592]]
      Predict: [[ True False False False False False]]
      [[0.62470267 0.42340335 0.36506738 0.4457744  0.4457744  0.4457744 ]]
      Predict: [[ True False False False False False]]
      [[0.59773301 0.41342558 0.37622192 0.43957601 0.43957601 0.43957601]]
      Predict: [[ True False False False False False]]
      [[0.56898076 0.40750965 0.38953048 0.43524027 0.43524027 0.43524027]]
      Predict: [[ True False False False False False]]
      [[0.53844771 0.40602534 0.40459143 0.43297485 0.43297485 0.43297485]]
      Predict: [[ True False False False False False]]
      [[0.50638194 0.40943245 0.42094353 0.43289126 0.43289126 0.43289126]]
      Predict: [[ True False False False False False]]
      [[0.47336687 0.4180945  0.43806331 0.43501625 0.43501625 0.43501625]]
      Predict: [[False False False False False False]]
      [[0.44034795 0.43197909 0.45501852 0.43926675 0.43926675 0.43926675]]
      Predict: [[False False False False False False]]
      [[0.42364049 0.44966395 0.47090266 0.44525181 0.44525181 0.44525181]]
      Predict: [[False False False False False False]]
      [[0.43180775 0.47034166 0.48645456 0.45191046 0.45191046 0.45191046]]
      Predict: [[False False False False False False]]
      [[0.43552928 0.48817335 0.49974213 0.45475436 0.45475436 0.45475436]]
      Predict: [[False False False False False False]]
      [[0.43645553 0.50194809 0.51114698 0.45649452 0.45649452 0.45649452]]
      Predict: [[False  True  True False False False]]
      [[0.43522132 0.51033459 0.52070943 0.45881942 0.45881942 0.45881942]]
      Predict: [[False  True  True False False False]]
      [[0.43228575 0.5126004  0.52840909 0.46275393 0.46275393 0.46275393]]
      Predict: [[False  True  True False False False]]
      [[0.42831486 0.50894535 0.53430355 0.46878662 0.46878662 0.46878662]]
      Predict: [[False  True  True False False False]]
      [[0.42432579 0.50065554 0.53862861 0.47690543 0.47690543 0.47690543]]
      Predict: [[False  True  True False False False]]
      [[0.42255534 0.49188901 0.54365781 0.48748557 0.48748557 0.48748557]]
      Predict: [[False False  True False False False]]
      [[0.42405041 0.48412107 0.54743276 0.49877814 0.49877814 0.49877814]]
      Predict: [[False False  True False False False]]
      [[0.42949333 0.47989662 0.54971396 0.50904414 0.50904414 0.50904414]]
      Predict: [[False False  True  True  True  True]]
      [[0.43915978 0.48121752 0.55036687 0.51659348 0.51659348 0.51659348]]
      Predict: [[False False  True  True  True  True]]
      [[0.45254606 0.48876639 0.54939318 0.52017404 0.52017404 0.52017404]]
      Predict: [[False False  True  True  True  True]]
      [[0.46836652 0.50155034 0.54696132 0.51943958 0.51943958 0.51943958]]
      Predict: [[False  True  True  True  True  True]]
      [[0.48491864 0.51718456 0.54338756 0.51519728 0.51519728 0.51519728]]
      Predict: [[False  True  True  True  True  True]]
      [[0.50055738 0.53266544 0.53905287 0.50920836 0.50920836 0.50920836]]
      Predict: [[ True  True  True  True  True  True]]
      [[0.51398613 0.54518682 0.53429175 0.50360739 0.50360739 0.50360739]]
      Predict: [[ True  True  True  True  True  True]]
      [[0.52431846 0.55264024 0.52931493 0.50027124 0.50027124 0.50027124]]
      Predict: [[ True  True  True  True  True  True]]
      [[0.53104431 0.55376295 0.5241984  0.50042027 0.50042027 0.50042027]]
      Predict: [[ True  True  True  True  True  True]]
      [[0.53400598 0.54811693 0.51892467 0.50447552 0.50447552 0.50447552]]
      Predict: [[ True  True  True  True  True  True]]
      [[0.53341713 0.53610319 0.51344526 0.51203632 0.51203632 0.51203632]]
      Predict: [[ True  True  True  True  True  True]]
      [[0.52993018 0.5191137  0.50774222 0.52187836 0.52187836 0.52187836]]
      Predict: [[ True  True  True  True  True  True]]
      [[0.52472628 0.49975195 0.50187682 0.5319945  0.5319945  0.5319945 ]]
      Predict: [[ True False  True  True  True  True]]
      [[0.5195332  0.48185125 0.49601486 0.53980193 0.53980193 0.53980193]]
      Predict: [[ True False False  True  True  True]]
      [[0.51640055 0.46991347 0.49041903 0.54264661 0.54264661 0.54264661]]
      Predict: [[ True False False  True  True  True]]
      [[0.51709881 0.4677986  0.48567399 0.53860398 0.53860398 0.53860398]]
      Predict: [[ True False False  True  True  True]]
      [[0.52073633 0.47371742 0.48127185 0.52572925 0.52572925 0.52572925]]
      Predict: [[ True False False  True  True  True]]
      [[0.53231446 0.49529906 0.47874048 0.51096054 0.51096054 0.51096054]]
      Predict: [[ True False False  True  True  True]]
      [[0.54282356 0.52012277 0.47686415 0.49262431 0.49262431 0.49262431]]
      Predict: [[ True  True False False False False]]
      [[0.55091527 0.54296661 0.4760187  0.47523695 0.47523695 0.47523695]]
      Predict: [[ True  True False False False False]]
      [[0.55575731 0.55930256 0.4762285  0.46261745 0.46261745 0.46261745]]
      Predict: [[ True  True False False False False]]
      [[0.5554765  0.56579529 0.47722584 0.45641854 0.45641854 0.45641854]]
      Predict: [[ True  True False False False False]]
      [[0.54925915 0.56065019 0.47876801 0.45743839 0.45743839 0.45743839]]
      Predict: [[ True  True False False False False]]
      [[0.53690438 0.54298992 0.48063403 0.46569212 0.46569212 0.46569212]]
      Predict: [[ True  True False False False False]]
      [[0.51849118 0.51292192 0.48266274 0.48024842 0.48024842 0.48024842]]
      Predict: [[ True  True False False False False]]
      [[0.49541711 0.47274902 0.48482527 0.49932837 0.49932837 0.49932837]]
      Predict: [[False False False False False False]]
      [[0.47103448 0.42872365 0.48717246 0.51989623 0.51989623 0.51989623]]
      Predict: [[False False False  True  True  True]]
      [[0.45119656 0.39196321 0.48972892 0.53755699 0.53755699 0.53755699]]
      Predict: [[False False False  True  True  True]]
      [[0.44315656 0.37616451 0.49233667 0.54705311 0.54705311 0.54705311]]
      Predict: [[False False False  True  True  True]]
      [[0.45176825 0.39995187 0.49459713 0.54365549 0.54365549 0.54365549]]
      Predict: [[False False False  True  True  True]]
      [[0.48103113 0.44904976 0.49568552 0.52978435 0.52978435 0.52978435]]
      Predict: [[False False False  True  True  True]]
      [[0.50196303 0.50261497 0.49496111 0.49817996 0.49817996 0.49817996]]
      Predict: [[ True  True False False False False]]
      [[0.52286876 0.55680121 0.4952448  0.46548277 0.46548277 0.46548277]]
      Predict: [[ True  True False False False False]]
      [[0.54370061 0.60438324 0.49661689 0.44128914 0.44128914 0.44128914]]
      Predict: [[ True  True False False False False]]
      [[0.56128987 0.64040216 0.49812296 0.42882277 0.42882277 0.42882277]]
      Predict: [[ True  True False False False False]]
      [[0.57398209 0.66371471 0.49970125 0.42899913 0.42899913 0.42899913]]
      Predict: [[ True  True False False False False]]
      [[0.57441645 0.66173445 0.49761128 0.43484764 0.43484764 0.43484764]]
      Predict: [[ True  True False False False False]]
      [[0.58324286 0.66349848 0.49577591 0.46472166 0.46472166 0.46472166]]
      Predict: [[ True  True False False False False]]
      [[0.58659821 0.65193511 0.48922812 0.50763148 0.50763148 0.50763148]]
      Predict: [[ True  True False  True  True  True]]
      [[0.58641052 0.62605182 0.48302131 0.56161491 0.56161491 0.56161491]]
      Predict: [[ True  True False  True  True  True]]
      [[0.57374846 0.56811291 0.45908349 0.59272877 0.59272877 0.59272877]]
      Predict: [[ True  True False  True  True  True]]
      [[0.44667831 0.52040553 0.44374188 0.54153458 0.54153458 0.54153458]]
      Predict: [[False  True False  True  True  True]]
      [[0.44614531 0.49155634 0.4394264  0.53121573 0.53121573 0.53121573]]
      Predict: [[False False False  True  True  True]]
      [[0.35736533 0.47504023 0.44080666 0.5101594  0.5101594  0.5101594 ]]
      Predict: [[False False False  True  True  True]]
      [[0.30251677 0.4728129  0.45010093 0.49135419 0.49135419 0.49135419]]
      Predict: [[False False False False False False]]
      [[0.3261351  0.47951403 0.46439393 0.50341604 0.50341604 0.50341604]]
      Predict: [[False False False  True  True  True]]
      [[0.30298609 0.46701296 0.47488244 0.48972562 0.48972562 0.48972562]]
      Predict: [[False False False False False False]]
      [[0.31859088 0.4502116  0.48856464 0.48586763 0.48586763 0.48586763]]
      Predict: [[False False False False False False]]
      [[0.34654907 0.44632814 0.50222032 0.46979442 0.46979442 0.46979442]]
      Predict: [[False False  True False False False]]
      [[0.41760303 0.4846852  0.51637477 0.47020021 0.47020021 0.47020021]]
      Predict: [[False False  True False False False]]
      [[0.47993359 0.52086618 0.52454201 0.45759751 0.45759751 0.45759751]]
      Predict: [[False  True  True False False False]]
      [[0.5272198  0.54470096 0.52940883 0.44128697 0.44128697 0.44128697]]
      Predict: [[ True  True  True False False False]]
      ANN arrived at conclusion: [[ True  True  True False False False]] after 83 iterations
      Test set 1: [[ True False  True  True]] from [[1 1]
       [0 0]
       [1 0]
       [0 1]]
      Test set 2: [[ True  True  True  True]] from [[0 1]
       [1 1]
       [1 1]
       [0 1]]
      Test set 3: [[ True  True  True  True]] from [[1 1]
       [1 1]
       [1 1]
       [1 1]]
      Test set 4: [[ True  True  True  True]] from [[0 1]
       [0 1]
       [0 1]
       [0 1]]
      Test set 5: [[False False False False]] from [[0 0]
       [0 0]
       [0 0]
       [0 0]]
      ```

4. Negation: set `learning_rate = 1.45`.

      ```bash
      python3 ml-negation.py

      Data entry 0&0 with label 1
      Data entry 1&1 with label 0
      [[0.5        0.60781839]]
      Predict: [[False  True]]
      [[0.50044067 0.59239116]]
      Predict: [[ True  True]]
      [[0.44496768 0.35093396]]
      Predict: [[False False]]
      [[0.45136722 0.26415482]]
      Predict: [[False False]]
      [[0.46197536 0.255857  ]]
      Predict: [[False False]]
      [[0.46203849 0.28229273]]
      Predict: [[False False]]
      [[0.45755148 0.34651838]]
      Predict: [[False False]]
      [[0.45733065 0.46150991]]
      Predict: [[False False]]
      [[0.4724445  0.62625429]]
      Predict: [[False  True]]
      [[0.52414063 0.67436868]]
      Predict: [[ True  True]]
      [[0.53844915 0.64200841]]
      Predict: [[ True  True]]
      [[0.61558185 0.61141409]]
      Predict: [[ True  True]]
      [[0.6815112  0.57167493]]
      Predict: [[ True  True]]
      [[0.71008336 0.52625786]]
      Predict: [[ True  True]]
      [[0.70974277 0.48345124]]
      Predict: [[ True False]]
      ANN arrived at conclusion: [[ True False]] after 14 iterations
      Test set 1: [[ True False]] from [[0 0]
       [1 1]]
      Test set 2: [[ True False  True False]] from [[0 0]
       [1 1]
       [0 0]
       [1 1]]
      Test set 3: [[False False False False]] from [[1 1]
       [1 1]
       [1 1]
       [1 1]]
      Test set 4: [[ True  True  True  True]] from [[0 0]
       [0 0]
       [0 0]
       [0 0]]
      ```

      > Note that `False` and `True` are modeled as: `[0, 0]` and `[1,1]`, respectively.

5. NAND: set `learning_rate = 1.175`

      ```bash
      python3 ml-nand.py

      Data entry 1&0 with label 1
      Data entry 0&1 with label 1
      Data entry 1&1 with label 0
      Data entry 0&0 with label 1
      Data entry 1&1 with label 0
      [[0.63767246 0.5        0.59235286 0.5        0.59235286]]
      Predict: [[ True False  True False  True]]
      [[0.66134185 0.51847616 0.67350126 0.54007131 0.67350126]]
      Predict: [[ True  True  True  True  True]]
      [[0.59342104 0.53531612 0.65618829 0.53333355 0.65618829]]
      Predict: [[ True  True  True  True  True]]
      [[0.49645589 0.53106508 0.57581129 0.5183503  0.57581129]]
      Predict: [[False  True  True  True  True]]
      [[0.45160645 0.53444472 0.50323834 0.52268195 0.50323834]]
      Predict: [[False  True  True  True  True]]
      [[0.43860289 0.55092789 0.46023867 0.53967998 0.46023867]]
      Predict: [[False  True False  True False]]
      [[0.4497723  0.57281358 0.44044255 0.56115066 0.44044255]]
      Predict: [[False  True False  True False]]
      [[0.46481511 0.59408675 0.42982669 0.58087936 0.42982669]]
      Predict: [[False  True False  True False]]
      [[0.47737196 0.6136568  0.42337418 0.59726687 0.42337418]]
      Predict: [[False  True False  True False]]
      [[0.4880123  0.6319401  0.42461952 0.61049883 0.42461952]]
      Predict: [[False  True False  True False]]
      [[0.49620888 0.64909903 0.43549042 0.62029088 0.43549042]]
      Predict: [[False  True False  True False]]
      [[0.50144781 0.66561167 0.45783992 0.62616717 0.45783992]]
      Predict: [[ True  True False  True False]]
      ANN arrived at conclusion: [[ True  True False  True False]] after 11 iterations
      Test set 1: [[False  True  True  True]] from [[1 1]
       [0 0]
       [1 0]
       [0 1]]
      Test set 2: [[ True False False  True]] from [[0 1]
       [1 1]
       [1 1]
       [0 1]]
      Test set 3: [[False False False False]] from [[1 1]
       [1 1]
       [1 1]
       [1 1]]
      Test set 4: [[ True  True  True  True]] from [[0 1]
      [0 1]
       [0 1]
       [0 1]]
      Test set 5: [[ True  True  True  True]] from [[0 0]
       [0 0]
       [0 0]
       [0 0]]
      Test set 6: [[False  True  True  True False  True  True  True False  True  True  True
      False  True  True  True]] from [[1 1]
       [0 0]
       [1 0]
       [0 1]
       [1 1]
       [0 0]
       [1 0]
       [0 1]
       [1 1]
       [0 0]
       [1 0]
       [0 1]
       [1 1]
       [0 0]
       [1 0]
       [0 1]]
      ```

6. XOR: set `1.155`
   
      ```bash
      python3 ml-xor.py

      Data entry 1&0 with label 1
      Data entry 0&1 with label 1
      Data entry 1&1 with label 0
      Data entry 0&0 with label 0
      Data entry 1&1 with label 0
      Data entry 1&0 with label 1
      Data entry 0&1 with label 1
      Data entry 1&1 with label 0
      Data entry 0&1 with label 1
      Data entry 0&0 with label 0
      Data entry 1&0 with label 1
      Data entry 0&0 with label 0
      Data entry 0&1 with label 1

      [[0.52160566 0.44295413 0.54657634 0.5        0.54657634 0.52160566
        0.44295413 0.54657634 0.44295413 0.5        0.52160566 0.5
        0.44295413]]
      Predict: [[ True False  True False  True  True False  True False False  True False
        False]]
      [[0.63949558 0.48711335 0.59751051 0.51231344 0.59751051 0.63949558
        0.48711335 0.59751051 0.48711335 0.51231344 0.63949558 0.51231344
        0.48711335]]
      Predict: [[ True False  True  True  True  True False  True False  True  True  True
        False]]
      [[0.69987554 0.51180049 0.62148149 0.52517796 0.62148149 0.69987554
        0.51180049 0.62148149 0.51180049 0.52517796 0.69987554 0.52517796
        0.51180049]]
      Predict: [[ True  True  True  True  True  True  True  True  True  True  True  True
         True]]
      [[0.7169037  0.5241609  0.6179902  0.52975462 0.6179902  0.7169037
        0.5241609  0.6179902  0.5241609  0.52975462 0.7169037  0.52975462
        0.5241609 ]]
      Predict: [[ True  True  True  True  True  True  True  True  True  True  True  True
         True]]
      [[0.70615874 0.55086346 0.58603203 0.52410009 0.58603203 0.70615874
        0.55086346 0.58603203 0.55086346 0.52410009 0.70615874 0.52410009
        0.55086346]]
      Predict: [[ True  True  True  True  True  True  True  True  True  True  True  True
         True]]
      [[0.68434138 0.54562133 0.52769492 0.50623664 0.52769492 0.68434138
        0.54562133 0.52769492 0.54562133 0.50623664 0.68434138 0.50623664
        0.54562133]]
      Predict: [[ True  True  True  True  True  True  True  True  True  True  True  True
         True]]
      [[0.68031778 0.53535909 0.48788968 0.49623155 0.48788968 0.68031778
        0.53535909 0.48788968 0.53535909 0.49623155 0.68031778 0.49623155
        0.53535909]]
      Predict: [[ True  True False False False  True  True False  True False  True False
        True]]
      ANN arrived at conclusion: [[ True  True False False False  True  True False  True False  True False
         True]] after 6 iterations

      Test set 1: [[False False True True]] from [[1 1]
      [0 0]
      [1 0]
      [0 1]]
      Test set 2: [[ True False False True]] from [[0 1]
      [1 1]
      [1 1]
      [0 1]]
      Test set 3: [[False False False False]] from [[1 1]
      [1 1]
      [1 1]
      [1 1]]
      Test set 4: [[ True True True True]] from [[0 1]
      [0 1]
      [0 1]
      [0 1]]
      Test set 5: [[False False False False]] from [[0 0]
      [0 0]
      [0 0]
      [0 0]]
      Test set 6: [[False False True True False False True True False False True True
      False False True True]] from [[1 1]
      [0 0]
      [1 0]
      [0 1]
      [1 1]
      [0 0]
      [1 0]
      [0 1]
      [1 1]
      [0 0]
      [1 0]
      [0 1]
      [1 1]
      [0 0]
      [1 0]
      [0 1]]
      ```

## An Alternative Approach

Before I got the **Learning Rates** correct, I was thinking it might be beyond my current skillset to *teach* an arbitrary machine how to do Boolean Algebra. Here's an alternative path/signpost, since **Negation** and **Conjunction** are 100% accurate one can interdefine the other two:

```plaintext
(A ∨ B) ≡ ¬(¬A ∧ ¬B)
(A → B) ≡ ¬(A ∧ ¬B)
```

> So, we could use the above if only two of the models worked (and the rest didn't). In any event, I got the above to work shortly after speculating about this.

## Academic Work

1. Cool paper on how to implement **Logic Learning Networks**: https://arxiv.org/pdf/1904.01554.pdf.
