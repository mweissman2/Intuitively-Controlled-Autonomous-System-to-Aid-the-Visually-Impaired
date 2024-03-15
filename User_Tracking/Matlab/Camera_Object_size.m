%calcuate size of face at different camera depths
%head_circumference = 56; %cm
head_width = 13; %cm
head_height = 15; %cm

HFOV = 90; %degrees
VFOV = 65; %degrees

HRES = [1280, 848, 640, 480, 424];
VRES = [720, 480, 360, 270, 240];

Distance = 50:1:400;
%horizontal
max_horizontal_cm = tand(HFOV/2)*Distance * 2;
h_head_size = head_width./max_horizontal_cm;

%vertical
max_vertical_cm = tand(VFOV/2)*Distance * 2;
v_head_size = head_height./max_vertical_cm;

%plot horizontal head size
my_legend = strings(1,length(HRES));
figure;
hold on
for i = 1:length(HRES)
    plot(Distance,h_head_size*HRES(i));
    my_legend(i) = [num2str(HRES(i)) 'p'];
end
hold off
title("Head Pixel Size vs distance from Camera");
xlabel("distance (cm)");
ylabel('Pixels for Head Width');
legend(my_legend)


%plot vertical head size
figure;
hold on
for i = 1:length(VRES)
    plot(Distance,v_head_size*VRES(i));
    my_legend(i) = [num2str(VRES(i)) 'p'];
end
hold off
title("Head Pixel Size vs distance from Camera");
xlabel("distance (cm)");
ylabel('Pixels for Head Height');
legend(my_legend)

%%
%calculate the depth camera DFOV
B = 9.5; %cm
HFOV = 87;
D_HRES = [1280, 848, 640, 480, 424];
DFOV = HFOV/2 +atan(tand(HFOV/2)- B./Distance);

my_legend = strings(1,length(HRES));

figure;
hold on
for i = 1:length(D_HRES)
    Ratio = D_HRES(i) * B./(2.*Distance*tand(HFOV/2));
    my_legend(i) = [num2str(D_HRES(i)) 'p'];
    plot(Distance,Ratio)
end
hold off
title('Ratio of Dead Band Depth vs Distance')
xlabel('Distance cm')
ylabel('Ratio')
legend(my_legend)

figure;
plot(Distance, DFOV);
title("Depth FOV vs Distance")
xlabel("Distance cm")
ylabel("DFOV")

