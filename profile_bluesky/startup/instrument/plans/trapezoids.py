import bluesky.plans as bp
import bluesky.plan_stubs as bps

__all__ = """
    trapezoid_plan
""".split()

def trapezoid_plan(detector_list = [varex, ptc10.temperatureB, ptc10.temperatureC,
                   ptc10.temperatureD], positioner_list = [ptc10], 
                   num_pts = {'up':10, 'plateau':10, 'down':10}.
                   interval_period = {'up': 60, 'plateau':60, 'down':60},
                   ramp_rate = {'up': 10, 'down':100}
                   target_pos = {'up': 800, 'down':20}
                   md = None):
            
    '''
    trapezoid plan executes a ramp up, plateau, and ramp down while triggering
    the first detector from the detector list and monitoring the remaining 
    detectors
    
    detector_list   : list of detectors with the first being an area detector
                      and the remaining being temperatures
    positioner_list : positioner, default is ptc10 which has been configured
                      as a positioner
    num_pts         : number of points to acquire during each phase in the 
                      form of a dictionary with keys up, plateau and down
    interval_period : amount of time between start of each measurement in the 
                      form of a dictionary with keys up, plateau and down
    ramp_rate       : rate of positioner in change in the form of a 
                      dictionary with keys up and down. Units are that of
                      the ramp rate PV.  For PTC10 this is K/min
    target_pos      : target position for positioner in the form of a 
                      dictionary with keys up and down. For the PTC, the 
                      units are degrees Celsius
    md              : extra metadata
    '''
    
    monitor_sig = detector_list[1:]
    
    def go_up():
        #set heating rate
        yield from bps.mv(positioner_list[0].ramp, ramp_rate['up'])

        #start heating but don't wait for completion
        yield from bps.mv(positioner_list[0].setPoint, target_pos['up'])
        
    def go_down():
        #set heating rate
        yield from bps.mv(positioner_list[0].ramp, ramp_rate['down'])

        #start heating but don't wait for completion
        yield from bps.mv(positioner_list[0].setPoint, target_pos['down'])
        
    def inner_plan():
        yield from bpS.one_shot([detector_list[0]])
    
    time_up = interval_period['up']*num_pts['up']*1.1 #adding 10% buffer    
    yield from bp.ramp_plan(go_up, monitor_sig, inner_plan,
                            take_pre_data=True, timeout=time_up, 
                            period=interval_period['up']
                            md = md)

    yield from bp.count(detector_list[0], num=num_pts['plateau'], 
                        delay=interval_period['plateau'], md = md)

    time_down = interval_period['down']*num_pts['down']*1.1 #adding 10% buffer  
    yield from bp.ramp_plan(go_down, monitor_sig, inner_plan,
                            take_pre_data=False, timeout=time_down, 
                            period=interval_period['down']
                            md = md)
