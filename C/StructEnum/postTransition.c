#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STRING_LENGTH 6

struct package
{
    char* id;
    int weight;
};

typedef struct package package;

struct post_office
{
    int min_weight;
    int max_weight;
    package* packages;
    int packages_count;
};

typedef struct post_office post_office;

struct town
{
    char* name;
    post_office* offices;
    int offices_count;
};

typedef struct town town;

void print_all_packages(town t) {
    printf("%s:\n", t.name);
    int num_offices = t.offices_count; 
    for(int i = 0; i < num_offices; i++){
        printf("\t%d:\n", i);
        int packs = t.offices[i].packages_count; 
        for(int j = 0; j < packs; j++){
            printf("\t\t%s\n",t.offices[i].packages[j].id);
        }
    }
}

void send_all_acceptable_packages(town* source, int source_office_index, town* target, int target_office_index) {    
    int i,j; 

    int tar_packs = target->offices[target_office_index].packages_count; 
    int src_packs = source->offices[source_office_index].packages_count; 

    int src_min_weight = source->offices[source_office_index].min_weight;
    int src_max_weight = source->offices[source_office_index].max_weight;
    int tar_min_weight = target->offices[target_office_index].min_weight; 
    int tar_max_weight = target->offices[target_office_index].max_weight;

    package *tmp_src_packages;
    // towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);
    // printf("SOURCE: \n");
    int sendable_packs = 0; 
    for(i = 0; i < src_packs; i++){
        // printf("%s %d\n",source->offices[source_office_index].packages[i].id,source->offices[source_office_index].packages[i].weight);
        int tmp_weight = source->offices[source_office_index].packages[i].weight; 
        if(tmp_weight >= tar_min_weight && tmp_weight <= tar_max_weight){
            sendable_packs++; 
        }
    }
    target->offices[target_office_index].packages = realloc(target->offices[target_office_index].packages, (tar_packs + sendable_packs) * sizeof(package));
    tmp_src_packages = malloc((src_packs - sendable_packs)*sizeof(package));
    int tmp_ind = 0; 
    for(i = 0; i < src_packs; i++){
        int tmp_weight = source->offices[source_office_index].packages[i].weight; 
        if(tmp_weight >= tar_min_weight && tmp_weight <= tar_max_weight){
            target->offices[target_office_index].packages[tar_packs++] = source->offices[source_office_index].packages[i];
        }
        else {
            tmp_src_packages[tmp_ind++] = source->offices[source_office_index].packages[i]; 
        }
    }
    source->offices[source_office_index].packages = realloc(source->offices[source_office_index].packages, (src_packs - sendable_packs)*sizeof(package));
    source->offices[source_office_index].packages = tmp_src_packages; 
    source->offices[source_office_index].packages_count = src_packs - sendable_packs; 
    target->offices[target_office_index].packages_count += sendable_packs; 
}

town town_with_most_packages(town* towns, int towns_count) {
    int i = 0; 
    int max_packs = 0; 
    town result; 
    for (i = 0; i < towns_count; i++){
        int j = 0;
        int num_packs_of_town = 0;  
        for(j = 0; j < towns[i].offices_count; j++){
            num_packs_of_town += towns[i].offices[j].packages_count;
        }
        if(max_packs < num_packs_of_town){
            max_packs = num_packs_of_town; 
            result = towns[i];
        }
    }
    return result;
}

town* find_town(town* towns, int towns_count, char* name) {
    int i; 
    town *result; 
    for(i = 0; i < towns_count; i++){
        if((!strcmp(name, towns[i].name)))
            result = towns + i;
    }
    return result;
}

int main()
{
    int towns_count;
    scanf("%d", &towns_count);
    town* towns = malloc(sizeof(town)*towns_count);
    for (int i = 0; i < towns_count; i++) {
        towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
        scanf("%s", towns[i].name);
        scanf("%d", &towns[i].offices_count);
        towns[i].offices = malloc(sizeof(post_office)*towns[i].offices_count);
        for (int j = 0; j < towns[i].offices_count; j++) {
            scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
            towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);
            for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
                towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
                scanf("%s", towns[i].offices[j].packages[k].id);
                scanf("%d", &towns[i].offices[j].packages[k].weight);
            }
        }
    }
    int queries;
    scanf("%d", &queries);
    char town_name[MAX_STRING_LENGTH];
    while (queries--) {
        int type;
        scanf("%d", &type);
        switch (type) {
        case 1:
            scanf("%s", town_name);
            town* t = find_town(towns, towns_count, town_name);
            print_all_packages(*t);
            break;
        case 2:
            scanf("%s", town_name);
            town* source = find_town(towns, towns_count, town_name);
            int source_index;
            scanf("%d", &source_index);
            scanf("%s", town_name);
            town* target = find_town(towns, towns_count, town_name);
            int target_index;
            scanf("%d", &target_index);
            send_all_acceptable_packages(source, source_index, target, target_index);
            break;
        case 3:
            printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
            break;
        }
    }

// mem free 
    for (int i = 0; i < towns_count; i++) {
        for (int j = 0; j < towns[i].offices_count; j++) {
            for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
                free(towns[i].offices[j].packages[k].id);
            }
            free(towns[i].offices[j].packages);
        }
        free(towns[i].name);
        free(towns[i].offices);
    }
    free(towns);



    return 0;
}


