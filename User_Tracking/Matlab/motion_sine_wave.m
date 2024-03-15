%motion sine wave
numpoints = 4;
t = linspace(0,4,numpoints);
tvec = linspace(0,4,numpoints*10);
x = linspace(0,4,numpoints);
y = 1.5*sin(2*pi*1/4.*t);

[q,qd,qdd,pp] = quinticpolytraj([x;y], t, tvec);

subplot(2,2,1)
plot(tvec, [q'])
legend(["x","y"])
xlabel('time (sec)')
ylabel('meters')


subplot(2,2,2)
plot(tvec, [qd'])
legend(["x\_dot","y\_dot"])
xlabel('time (sec)')
ylabel('m/s')

subplot(2,2,3)
plot(tvec, [qdd'])
legend(["x\_ddot","y\_ddot"])
xlabel('time (sec)')
ylabel('m/s^2')

subplot(2,2,4)
plot(q(1,:)',q(2,:)')
xlabel('X position')
ylabel('y position')

%% deceleration

numpoints = 2;
t = linspace(0,0.5,numpoints)
tvec = linspace(0,0.5,numpoints*10);
x = linspace(0.5,0,numpoints);
y = linspace(0.5,0,numpoints);

[q,qd,qdd,pp] = quinticpolytraj([x;y], t, tvec);

subplot(2,2,1)
plot(tvec, [q'])
legend(["x","y"])
xlabel('time (sec)')
ylabel('meters')


subplot(2,2,2)
plot(tvec, [qd'])
legend(["x\_dot","y\_dot"])
xlabel('time (sec)')
ylabel('m/s')

subplot(2,2,3)
plot(tvec, [qdd'])
legend(["x\_ddot","y\_ddot"])
xlabel('time (sec)')
ylabel('m/s^2')

subplot(2,2,4)
plot(q(1,:)',q(2,:)')
xlabel('X position')
ylabel('y position')