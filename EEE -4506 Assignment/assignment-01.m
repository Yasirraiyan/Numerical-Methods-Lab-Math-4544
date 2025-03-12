% ডেটা তৈরি
x = 0:0.1:10;
y1 = sin(x);
y2 = cos(x);
y3 = tan(x);
y4 = exp(-x);

% ফিগার তৈরি
figure;

% প্রথম subplot (1st plot)
subplot(2, 2, 1); % 2 rows, 2 columns, 1st plot
plot(x, y1);
title('Sin(x)');

% দ্বিতীয় subplot (2nd plot)
subplot(2, 2, 2); % 2 rows, 2 columns, 2nd plot
plot(x, y2);
title('Cos(x)');

% তৃতীয় subplot (3rd plot)
subplot(2, 2, 3); % 2 rows, 2 columns, 3rd plot
plot(x, y3);
title('Tan(x)');

% চতুর্থ subplot (4th plot)
subplot(2, 2, 4); % 2 rows, 2 columns, 4th plot
plot(x, y4);
title('Exp(-x)');
